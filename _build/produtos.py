P = """Cinta Abdominal|49,99
Cinta Pós-Cirúrgica|54,99
Maiô Tricot Chevron|139,99
Sutiã|79,99
Cinta Modeladora Tunísia|49,99
Sutiã Microfibra Avulso|49,99
Conjunto Renda Bojo|79,99
Camisola Lully Liganete|49,99
Biquíni Regulador|59,99
Biquíni Top Faixa|49,99
Calcinha Cotton Clássica|32,99
Calcinha Caleçon Soft|34,99
Saída de Praia Crochê|56,99
Saída de Praia Mini|29,99
Saída de Praia Regata|29,99
Sutiã Multiforms|99,00
Conjunto Charlote|59,99
Saída de Praia Top|49,99
Top Faixa de Renda Bandeau|49,99
Top Bustier com Bojo|89,99
Conjunto Top Rendado|59,99
Conjunto Valentina|54,99
Conjunto Carol Branco|84,99
Protetor de Silicone|44,99
Sutiã Básico com Bojo|64,99
Bermuda Classic|36,99
Cropped|49,99
Top em Microfibra|59,99
Cinta Modeladora|54,99
Shorts Microfibra|29,99
Conjunto Sofie|84,99
Body|49,99
Body Isis de Renda|49,99
Conjunto Camila Rubi|79,99
Biquíni Bojo|79,99
Vestido Saída Mali|119,99
Bolsa Tricot Chevron|139,99
Sutiã Triângulo Mate|49,99
Body Essencial|49,99
Saída de Praia Mangas|99,00
Conjunto Baby-doll|49,99
Short Skin Touch|39,99
Blusa Tule|79,99
Bermuda Modeladora|69,99
Calcinha Regulável|14,99
Calcinha Hot Mate|49,99
Kit Calcinhas Biquíni Nature|24,99
Calcinha Alta Nature|29,00
Biquíni Trilobal|49,99
Saída de Praia Conjunto|39,99
Biquíni|149,99
Saída de Praia Pareô|79,99
Saída de Praia Macacão|54,99
Conjunto Sainha - Kit 3 peças|144,99
Calça Cintura Alta|79,99
Camisa Infantil|39,99
Baby-doll|49,99
Body Tule com Renda|59,99
Conjunto Fitness Cropped|139,99
Conjunto Biquíni Meia Taça|139,99
Short no Linho|99,99
Acessório Bandana|54,99
Sutiã Tomara que Caia|54,99
Conjunto Luxo|159,99
Conjunto Plus|69,99
Camiseta Fitness|59,99
Biquíni Tomara que Caia Alças|179,99
Biquíni Cortininha|169,99
Biquíni Meia Taça|159,80
Conjunto Biquíni Cortininha|159,99
Pijama de Inverno|110,00
Pijama de Inverno|119,99
Cinta Calcinha Ghana|49,99
Conjunto Thaís|84,99
Macaquinho Fitness|139,99
Conjunto Carol Preto|84,99
Conjunto Zara|249,00
Conjunto Top Tendado|54,99
Bermuda Anágua|49,99
Conjunto Camila Luxo|84,99
Conjunto Tule sem Bojo|24,99
Calesson|22,99
Top Skin Up|99,99
Conjunto Noivinha|54,99
Saída de Praia Macacão|39,99
Shorts Anágua|49,99
Calcinha Microfibra|18,99
Conjunto Plus|74,99
Conjunto sem Bojo|54,99
Conjunto Lingerie|29,99
Sutiã Avulso Laura|59,99
Calça Tule Crochê|139,99
Conjunto Francesca|59,99
Body Xadrez Preto|49,99
Biquíni Crochê Azul|99,99
Conjunto Isadora Renda|24,99
Camisola Luxo|99,00
Sutiã Sustent|69,99
Conjunto Paloma|49,99
Robe Emile|69,99
Conjunto Rebeca|54,99
Sutiã Comfort Slim|99,00
Conjunto Biquíni Fita|64,99
Conjunto Sutiã Aro|54,99
Conjunto Rendado|49,99
Shortdoll Eliane Animal Print|49,99
Calcinha|24,99
Calcinha Márcia|22,99
Saia Curta com Franja|159,99
Conjunto Peluciado|119,99
Camisola Joelma Preta|79,99
Saída de Praia Vestido|49,99
Calcinha Fio Duplo|17,99
Cropped Renda|69,99
Calcinha Gabi|14,99
Robe Laila em Liganete|89,99
Pareô|89,99
Conjunto Dayse|69,99
Baby-doll|29,99
Óculos Avante|99,00
T-shirt Alongada|69,99
Conjunto Baby-doll|49,99
Conjunto Livia|54,99
Camisola Geórgia|79,99
Vestido Tubinho|39,99"""
PRODUTOS=[(i+1,l.split('|')[0],float(l.split('|')[1].replace(',','.'))) for i,l in enumerate(P.splitlines())]
assert len(PRODUTOS)==125, len(PRODUTOS)
