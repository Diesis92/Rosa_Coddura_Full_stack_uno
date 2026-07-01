-- ============================================================
-- ShopBot RAG — Schema MySQL
-- Eseguito automaticamente al primo avvio del container MySQL
-- ============================================================

CREATE DATABASE IF NOT EXISTS shopbot
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE shopbot;

CREATE TABLE IF NOT EXISTS prodotti (
  id           INT AUTO_INCREMENT PRIMARY KEY,
  nome         VARCHAR(200)   NOT NULL,
  descrizione  TEXT           NOT NULL,
  categoria    VARCHAR(100)   NOT NULL,
  prezzo       DECIMAL(10,2)  NOT NULL,
  disponibile  TINYINT(1)     NOT NULL DEFAULT 1,
  tag          VARCHAR(500)   NOT NULL DEFAULT '',
  updated_at   TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP
                              ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================
-- 20 prodotti di esempio
-- ============================================================

INSERT INTO prodotti (nome, descrizione, categoria, prezzo, disponibile, tag) VALUES

('Salomon X Ultra 4 GTX',
 'Scarpa da trekking impermeabile con membrana GORE-TEX. Suola Contagrip per grip su terreni bagnati e rocciosi. Leggera e stabile.',
 'calzature', 189.99, 1, 'trekking,impermeabile,gore-tex,montagna,escursionismo'),

('Columbia Redmond V2 WP',
 'Scarpa da camminata impermeabile con tecnologia OutDry. Ideale per sentieri e camminate in ambiente umido. Ottimo rapporto qualità-prezzo.',
 'calzature', 99.95, 1, 'impermeabile,camminata,sentieri,outdry,economica'),

('Nike React Infinity Run',
 'Scarpa da running con ammortizzazione React per lunghe distanze. Design stabile che riduce il rischio di infortuni. Adatta ad asfalto.',
 'calzature', 159.99, 1, 'running,corsa,ammortizzazione,asfalto,lunga-distanza'),

('Adidas Terrex Swift R3',
 'Trail running shoe tecnica per percorsi misti. Suola Continental per trazione su bagnato. Leggera e reattiva.',
 'calzature', 139.99, 0, 'trail,running,tecnica,continental,bagnato'),

('The North Face Resolve 2 Jacket',
 'Giacca antipioggia leggera e comprimibile. Tessuto DryVent impermeabile e traspirante. Ideale per escursioni e viaggi.',
 'abbigliamento', 119.00, 1, 'giacca,impermeabile,antipioggia,leggera,dryvnet,escursioni'),

('Patagonia Nano Puff Jacket',
 'Piumino sintetico ultraleggero con isolamento PrimaLoft. Mantiene il calore anche bagnato. Ottimo layer intermedio.',
 'abbigliamento', 229.00, 1, 'piumino,caldo,primaloft,sintetico,leggero,layer'),

('Decathlon Forclaz Trek 100',
 'Pantalone da trekking modulare con zip per conversione in shorts. Tessuto rapido-asciutto. Economico e versatile.',
 'abbigliamento', 34.99, 1, 'pantaloni,trekking,modulare,economico,versatile'),

('Icebreaker Merino 200 Oasis',
 'Maglia base layer in lana merino 200g. Termoregolante, antibatterica, non prude. Ideale per trekking e sci.',
 'abbigliamento', 89.00, 1, 'merino,lana,base-layer,termico,antibatterico,sci,trekking'),

('Osprey Atmos AG 65',
 'Zaino da trekking 65 litri con sistema Anti-Gravity per distribuzione del peso. Ideale per trekking di più giorni.',
 'zaini', 349.00, 1, 'zaino,65L,trekking,anti-gravity,multigiorno,osprey'),

('Deuter Speed Lite 20',
 'Zaino leggero da 20 litri per escursioni giornaliere. Schienale aerato e bretelle imbottite. Tasca idratazione compatibile.',
 'zaini', 89.90, 1, 'zaino,20L,escursionismo,leggero,day-hike,idratazione'),

('Quechua NH Arpenaz 30',
 'Zaino da 30 litri per trekking entry-level. Cover antipioggia inclusa. Buon volume al prezzo più basso della categoria.',
 'zaini', 29.99, 1, 'zaino,30L,economico,entry-level,cover-pioggia'),

('MSR Hubba Hubba NX 2',
 'Tenda ultraleggera a 2 posti da 1.7 kg. Doppia parete, facile da montare. Ideale per backpacking e trekking.',
 'campeggio', 549.00, 1, 'tenda,2posti,ultraleggera,backpacking,doppia-parete'),

('Sea to Summit Spark SP1',
 'Sacco a pelo ultraleggero per temperature fino a +4°C. Riempimento in piuma 850 FP. Compressione estrema.',
 'campeggio', 279.00, 0, 'sacco-pelo,leggero,piuma,caldo,850fp,comprimibile'),

('Jetboil Flash',
 'Fornelletto a gas integrato con sistema di cottura ultrarapido. Boil time 100 secondi per 0.5L. Indispensabile in alta quota.',
 'campeggio', 129.95, 1, 'fornello,cottura,rapido,gas,ultraleggero,alta-quota'),

('Black Diamond Spot 400',
 'Frontale LED da 400 lumen con batterie ricaricabili. Modalità rossa per visione notturna. Impermeabile IPX8.',
 'campeggio', 49.95, 1, 'frontale,led,400lumen,ricaricabile,impermeabile,notturno'),

('Garmin inReach Mini 2',
 'Comunicatore satellitare bidirezionale con GPS. Invia messaggi e tracce ovunque nel mondo senza copertura GSM.',
 'sicurezza', 399.00, 1, 'satellitare,gps,comunicatore,emergenza,tracciamento,garmin'),

('Suunto Core All Black',
 'Orologio outdoor con altimetro, barometro e bussola. Impermeabile 30m. Ideale per trekking e alpinismo.',
 'sicurezza', 179.00, 1, 'orologio,altimetro,barometro,bussola,impermeabile,alpinismo'),

('Hydrapack Shape-Shift 8L',
 'Zaino da trail running 8L con sistema idratazione 1.5L integrato. Leggero, aderente, perfetto per corse lunghe.',
 'idratazione', 119.00, 1, 'idratazione,trail,corsa,8L,leggero,running'),

('Katadyn BeFree 1L',
 'Borraccia filtrante da 1 litro. Filtra batteri e protozoi dal 99.9%. Nessun gusto chimico. Ideale per sorgenti.',
 'idratazione', 44.95, 1, 'borraccia,filtrante,purificazione,sorgente,batteri,protozoi'),

('Black Diamond Trail Back',
 'Bastoncini da trekking in alluminio con grip in sughero. Sistema Flick Lock per regolazione rapida. Coppia 180g.',
 'accessori', 79.95, 1, 'bastoncini,trekking,alluminio,sughero,regolabile,coppia');
