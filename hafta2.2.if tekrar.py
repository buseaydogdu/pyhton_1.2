print("chat gptv'ye hoş geldin")

cevap=input("nasılsın")
# if cevap == 'iyiyim' or cevap =='iyi' #cevap iyiyimse ya da cevap iyiyse
if cevap in ['iyiyim','iyi','güzel']: #bu ve üst satır aynı işi yapar.
    print("güzel. iyi olmana sevindim")

if cevap in ['kötü','moralim bozuk']:  #cevap bunlardan biriyse
    c= input('hayırdır ne oldu?')
    if c in ['sınavım kötü geçti','sınav kötüydü']:
        print('böyle şeyleri takma.')
    if c in ['otobüsü kaçırdım','sınav kötüydü']:
        print('sonraki sefere, olmaz ins.')
        
input()
