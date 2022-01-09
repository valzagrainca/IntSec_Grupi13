# Universiteti i Prishtinës - FIEK
## Lënda: Siguria në Internet, Grupi: 13
## Zhvillimi i një API me disa funksione bazike, duke implementuar autentifikimin bazik ose me token

* Realizimi i kësaj detyre është bërë me anë të gjuhës programuese Python andaj paraprakisht duhet ta keni të instaluar Python3

### Çka është një API ?
 API qëndron për Application Program Interface. Merr mesazhet të cilat i dërgon në sistem dhe kthen përgjigjien nga sistemi. Pra, është një ndërmjetësues në mes nesh dhe sistemit.

\
&nbsp;

### GUI - Graphical User Interface në Python
#### Çka është GUI ?
>> Ndërfaqja grafike e përdoruesit (GUI) është një formë e ndërfaqes që i lejon përdoruesit të ndërveprojnë me pajisjet elektronike përmes ikonave grafike si butona, meny, fusha për insertimin e të dhënave. 
>> Në Python kjo realizohet përmes librarise Tkinter paraprakisht të instaluar në Python 3, librari mjaft e thjeshtë dhe mjaft fleksibile.
>>> Disa nga metodat e përdorura nga kjo librari:
>>> - Buttons -> Shfaq butona pra paraqet një mënyrë për të komunikuar me shfrytëzuesit
>>> - Entry –> Përdoret për të marrë të dhëna nga përdoruesi përmes User Inteface (shfaqet një kuti e thjeshtë ku përdoruesi jep tekst)
>>> - Label –> Përdoret për të shfaqur tekst në GUI
>>> - Canvas –> Përdoret për të vizatuar grafikë dhe skema
>>> - Frame –> Skicon kornizën për dritaren Tkinter me madhësi fikse

\
&nbsp;
 
### JWT - JSON Web Token
#### Çka është JWT ?
> JSON Web Token (JWT) është një standard i hapur (RFC 7519) që përcakton një mënyrë kompakte dhe të pavarur për transmetimin e sigurt të informacionit midis palëve si një objekt JSON.
#### Si funksionon në programin tonë ?
> Për çdo përdorues që logohet duke dhënë emrin dhe password-in, në rast suksesi lëshohet një token i nënshkruar i cili përdoret për autentifikimin e shfrytëzuesit.
> Jwt është nënshkruar me qelësin sekret publik,dhe algoritmi i përdorur është HS256.

\
&nbsp;
 
### Përdorimi
#### Parakushtet
>> Parakushtet për funksionimin e kësaj detyre:
>>> * Download-imi i kodit nga Github
>>> * Pajisja me një IDE ku mund të ekzekutohet kodi në python
>>> * Libraritë e veçanta për ekzekutim (që nuk janë të parainstaluara)
#### Përshkrimi i përdorimit
>> Përdoruesit i mundësohen tri pamje në menu:
>>> - Register (nëse përdoruesi nuk është regjistruar më herët mund të kalojë në këtë pamje)
>>> - Login with password (nëse përdoruesi ka pasur më herët llogari të hapur atëherë mund të behet login nga ku i hapet pamja e ashtuquajtur online)
>>> - Login with token (ofron mundësinë e qasjes me token të gjeneruar automatikisht)

\
&nbsp;
 
### Realizimi
#### Si është implementuar API ?
>> Modulet e pamjes dhe eventeve janë të ndarë në dy files të veçantë si:
>>> * screen.py 
>>> * event.py
>> E më pas ekzekutimi i programit bëhet në file-in app.py.
#### Vërtetimi i përdoruesit
>> - Së pari hapet pamja login with password për përdoruesit të cilët vetëm se janë të regjistruar. Në rast se përdoruesi nuk ekziston ose fjalëkalimi nuk përputhet atëherë kthejmë përgjigjen me mesazh gabimi.
>> - Nëse përdoruesi nuk ekziston atëherë duhet regjistruar te pamja regjistër. Pas regjistrimit krijojmë një token si payload ku ruhet emri i përdoruesit për të identifikuar përdoruesin e me pas enkodojmë payload-in me një string sekret dhe algoritëm të specifikuar.
>> - Edhe për dekodim të token-it (gjatë kyçjes me token) përdorim të njëjtin string sekret dhe algoritmin e specifikuar, në rast se tokeni nuk është i njëjtë atëherë kthejmë përgjigjen me mesazh gabimi.
