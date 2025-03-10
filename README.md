# Bot do Discord - Calendário de Aulas

## Sobre o Projeto
Este bot permite exibir um calendário semanal de aulas no Discord. Os usuários podem interagir com um botão para visualizar uma imagem do calendário diretamente no chat.

## Funcionalidades
- Exibe um embed com informações sobre as aulas.
- Botão interativo para exibir uma imagem do calendário.
- Personalização do status do bot.

## Como Instalar e Rodar
1. **Instale as dependências**:
   ```sh
   pip install -r requirements.txt
   ```
2. **Configure o bot**:
   - Crie um bot no [Discord Developer Portal](https://discord.com/developers/applications)
   - Copie o token gerado e substitua `'sua key aqui'` no arquivo `bot.py`.
   
3. **Execute o bot**:
   ```sh
   python bot.py
   ```
4. **Adicione o bot ao servidor**:
   - Gere um link de convite e conceda permissões necessárias.

## Uso
- Digite `!calendario` no chat para exibir o calendário.
- Clique no botão "📅 Calendário" para visualizar a imagem.

## Personalização
- Edite `image_url` no código para alterar a imagem do calendário.
- Modifique o texto do embed no comando `!calendario`.

## Problemas Comuns
- **Bot não responde?** Verifique as permissões no servidor.
- **Erro de token?** Certifique-se de que o token está correto e ativo.

## Licença
Este projeto é de uso livre e pode ser modificado conforme necessário. Apenas deixe os creditos.
