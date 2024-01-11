PROJETO PROGRAMAÇÃO PARA REDES 2023.2
 
 
- OBJETIVO
1. Projeto de aplicação Cliente/Servidor em python utilizando Sockets TCP. Utilizaremos o TCP para garantir uma comunicação confiável, garantindo que os dados sejam entregues sem perdas. Apesar do TCP ser mais lento que o UDP, nessa aplicação será suficiente para os nossos requisitos.
 

- APLICAÇÃO CLIENTE
1. Informará ao servidor que ele está on-line, informando o nome do HOST do cliente, seu IP e usuário logado;
2. Executado em segundo plano;
3. Caso o servidor não esteja on-line, o cliente ficará rodando em segundo plano testando a cada tempo pré-determinado se o servidor voltou a ficar on-line;
4. Enquanto estiver na memória o agente deverá responder a requisições oriundas do servidor;
 

- APLICAÇÃO SERVIDOR
1. Permite conexão oriunda de vários clientes simultaneamente;
2. Gerenciar as conexões ativas e detectar quando um cliente ficar off-line;
3. Executado em segundo plano;
4. Não permite que uma segunda instância dele seja carregado na memória;

  
- BOT TELEGRAM
1. Utilizaremos um BOT telegram como intermediador entre o cliente e o servidor. Os comandos de comunicação entre o cliente e o servidor serão chamados atrável do BOT.
