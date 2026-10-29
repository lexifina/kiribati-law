"""Parse cache/order.xml (legislation.gov.uk, SI 1979/719 as made) into corpus.json. Deterministic; no network."""
import hashlib, json, re
from pathlib import Path
from lxml import etree
here = Path(__file__).parent
NS = '{http://www.legislation.gov.uk/namespaces/legislation}'
raw = (here / 'cache' / 'order.xml').read_bytes()
root = etree.fromstring(raw)
def ln(e): return etree.QName(e).localname
def tx(e):
    s = ' '.join(''.join(e.itertext()).split())
    s = s.replace(' ', ' ').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return s
def child(e, name):
    for c in e:
        if ln(c) == name: return c
def paralines(para):
    out = []
    for c in para:
        n = ln(c)
        if n in ('P2', 'P3', 'P4', 'P5'):
            num = tx(child(c, 'Pnumber'))
            sub = [x for x in c if ln(x).endswith('para')]
            inner = []
            for s in sub: inner += paralines(s)
            if not inner: inner = ['']
            inner[0] = '(%s) %s' % (num, inner[0])
            out += ['  ' + l if i else l for i, l in enumerate(inner)] if False else inner
        elif n == 'Text':
            if len(c.findall(NS + 'Definition')) > 1:
                out += re.split(r'(?<=;) (?=")', tx(c))
            else:
                out.append(tx(c))
        elif n == 'Pnumber':
            continue
        else:
            out.append(tx(c))
    return out
be = root.find('.//' + NS + 'BlockExtract')
part = be[0]
units = {}
pre = [tx(c) for c in part if ln(c) == 'P']
decl = [c for c in part if ln(c) == 'P1']
lines = ['# Preamble', pre[0], pre[1]] + ['(%s) %s' % (tx(child(c, 'Pnumber')), tx(c.find(NS + 'P1para'))) for c in decl]
units['preamble'] = {'label': 'Preamble', 'kind': 'preamble', 'text': '\n'.join(lines) + '\n'}
ROM = {}
for ch in [c for c in part if ln(c) == 'Chapter']:
    num = tx(child(ch, 'Number')); title = tx(child(ch, 'Title'))
    k = int(re.sub(r'\D', '', '0' + {'CHAPTER 1': '1'}.get(num, '')) or 0) or None
    word = num.split()[-1]
    rom = {'1': 1, 'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}[word]
    units['chapter-%02d' % rom] = {'label': 'Chapter %d' % rom, 'kind': 'chapter', 'text': '# Chapter %d\n%s\n' % (rom, title.title() if title.isupper() else title)}
    for g in ch.iter(NS + 'P1group'):
        title_g = tx(child(g, 'Title'))
        for p in g.findall(NS + 'P1'):
            n = int(tx(child(p, 'Pnumber')))
            body = []
            for s in p:
                if ln(s) == 'P1para': body += paralines(s)
            units['sec-%03d' % n] = {'label': 'Section %d' % n, 'kind': 'sec', 'text': '\n'.join(['# %d. %s' % (n, title_g)] + body) + '\n'}
sched2 = [c for c in be if ln(c) == 'Schedule'][1]
sb = child(sched2, 'ScheduleBody')
sl = ['# Schedule 2. Territory of Kiribati', 'Section 132']
for p in sb:
    for c in p:
        if ln(c) == 'Text': sl.append(tx(c))
        elif ln(c) == 'UnorderedList':
            for li in c.iter(NS + 'Text'): sl.append(tx(li))
        else: sl.append(tx(c))
units['schedule-2'] = {'label': 'Schedule 2', 'kind': 'schedule', 'text': '\n'.join(sl) + '\n'}
url = 'https://www.legislation.gov.uk/uksi/1979/719/made'
corpus = {
 'country': {'code': 'KI', 'name': 'Kiribati', 'slug': 'kiribati', 'lang': 'en', 'tz': 'Pacific/Tarawa', 'future_branch': 'future',
   'publisher': {'name': 'The National Archives (legislation.gov.uk)', 'email': 'tna@legislation.gov.uk.invalid'},
   'default_in_force_rule': {'text': 'The Constitution came into force at independence on 12 July 1979 (Kiribati Independence Order 1979, article 1 and section 1 of the Kiribati Act 1979 context; legislation.gov.uk records the coming-into-force date).', 'source': url},
   'licence_note': 'Contains public sector information licensed under the Open Government Licence v3.0 (legislation.gov.uk, The National Archives).'},
 'sources': [{'name': 'legislation.gov.uk: The Kiribati Independence Order 1979 (SI 1979/719), as made', 'url': url, 'retrieved': '2026-10-29',
   'licence': 'Open Government Licence v3.0', 'notes': 'XML of the Order as made. The Constitution of Kiribati is Schedule 2 to the Order (the Schedule to the Order).'}],
 'laws': {'si-1979-719': {'label': 'SI 1979/719', 'title': 'The Kiribati Independence Order 1979', 'kind': 'decree', 'enacted': '1979-06-26', 'published': '1979-07-04', 'url': url,
   'temporary_until': None, 'restores': None, 'note': None}},
 'acts': [{'slug': 'constitution', 'short': 'Constitution', 'title': 'Constitution of Kiribati (as made, 1979)', 'url': url, 'first_law': 'si-1979-719', 'earlier_laws': [],
   'versions': [{'from': '1979-07-12', 'source_url': url + '/data.xml', 'sha256': hashlib.sha256(raw).hexdigest(), 'units': units,
     'credits': {k: ['si-1979-719'] for k in units},
     'note': 'The Constitution as made by the Kiribati Independence Order 1979. Amendments since 1979 (for example 1995, 2013, 2018) are not in this record.'}]}],
 'applies': [],
 'decisions': ['Only the Constitution as made (Schedule to the Order, in force 12 July 1979) is built; it is the only official text found online. The Kiribati government site and PacLII were not used (PacLII robots.txt disallows AI crawlers).',
   'Schedule 1 (oaths and affirmations) is published only as images, so it is left out (no OCR). Part headings inside chapters are left out; chapter titles are kept.',
   'Order date 26 June 1979 and publication date 4 July 1979 are from the legislation.gov.uk metadata; the Constitution took effect at independence on 12 July 1979.'],
 'ai_use': ['Claude Code wrote the parser; it did not write or alter any legal text.']}
(here / 'corpus.json').write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
print(len(units), list(units)[:5])
