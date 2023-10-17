import pandas as pd
from twilio.rest import Client

# Informação do Twilio
# Your Account SID and Auth Token from console.twilio.com
account_sid = "AC4443f31aaabd1420ce721463858f5ad6"
auth_token  = "41c4d2740083aaabedd429bb4630378c"

client = Client(account_sid, auth_token)


# PROBLEMA: avisar quando UM vendedor atingir R$55k no mes via sms
# passo a passo para solução
# abrir os arquivos em excel
# print(tabelas_venda)
# verificar se algum valor na coluna Vendas é maior que 55k
# se for maior -> enviar sms com o nome, mes e vendas do vendedor

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tab_vendas = pd.read_excel(f'.\planilhas\{mes}.xlsx')
    if (tab_vendas['Vendas'] > 55000).any():
        vendedor = tab_vendas.loc[tab_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        
        vendas = tab_vendas.loc[tab_vendas['Vendas'] > 55000,'Vendas'].values[0]
       
        msn = f'No mês {mes} alguem bateu a meta. Vendendor: {vendedor}; Venda: R$ {vendas:.2f}'
        
        message = client.messages.create(
            to="+5571992951939",
            from_="+15672296925",
            body=msn)

        print(message.sid)
