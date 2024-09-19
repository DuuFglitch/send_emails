import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import Tk, Label, Button, StringVar, OptionMenu, messagebox

def enviar_email():
    mes = mes_var.get()
    assunto = f"Solicitação de documentos - {mes}"
    tipo_email = tipo_email_var.get()

    if tipo_email == "EMAIL 1 - Antes do dia 10":
        corpo_email = (f"""<html>
        <body>
            <p>Prezado cliente,</p>
            <p>No intuito de mantermos a contabilidade de sua empresa em dia, solicito que envie a documentação ref. ao mês de 
            <b>{mes}</b>, sendo eles:</p>
            <ul>
                <li>Documentos ou Planilha Financeira preenchida com todas as despesas incorridas no mês.</li>
                <li>Extratos bancários nos formatos PDF e OFX.</li>
                <li>Caso tenham contratado algum tipo de empréstimo, seguro (gentileza enviar documento pertinente).</li>
            </ul>
            <p><span style="color: red;">Importante lembrar que precisamos dessa documentação até o dia 10 para que tenhamos tempo hábil para escriturar e oferecer relatórios tempestivos caso seja necessário.</span></p>
            <p><u>Qualquer dúvida, encontramo-nos à disposição.</u></p>
            <p><u>Gentileza confirmar o recebimento deste.</u></p>
            <p>At.te.</p>
        </body>
        </html>""")
    elif tipo_email == "EMAIL 2 - Após o dia 10":
        corpo_email = (f"""<html>
        <body>
            <p>Prezado cliente,</p>
            <p>No início do mês solicitamos o envio da documentação contábil referente ao período de <b>{mes}</b> para devida escrituração, porém não tivemos nenhum retorno sobre.</p>
            <p>Segue novamente a relação de documentos:</p>
            <ul>
                <li>Extratos bancários nos formatos PDF e OFX.</li>
                <li>Documentos ou Planilha Financeira preenchida com todas as despesas incorridas no mês – Caso necessite, entre em contato para auxílio no preenchimento.</li>
                <li>Caso tenham contratado algum tipo de empréstimo, seguro – gentileza enviar documento pertinente.</li>
            </ul>
            <p><span style="color: red;">Importante lembrar que precisamos dessa documentação até o dia 10 de cada mês para que tenhamos tempo hábil para escriturar e oferecer relatórios tempestivos caso seja necessário.</span></p>
            <p><u>Qualquer dúvida, encontramo-nos à disposição.</u></p>
            <p><u>Gentileza confirmar o recebimento deste.</u></p>
            <p>At.te.</p>
        </body>
        </html>""")

    # Listas de destinatários
    destinatarios_bcc = ['financeiro@plenumsistemas.com.br,padariabiopao@gmail.com,letrigalle@gmail.com,financeiromotelfantasy1@gmail.com, financeiromoteisfantasy@gmail.com, fiscal.frigolucio@gmail.com, grupo.padalitamary20@yahoo.com,  administrativo.ribeiraodasneves@apaemg.org.br,diretoria@hotel7colinas.com.br,controladoria@hotel7colinas.com.br,hmfdistribuidora@hotmail.com,frigocampos1@gmail.com,anderson@3campos.com.br,financeiro@3campos.com.br']# Substitua pelos e-mails reais
    destinatarios_principais = ['contabil03@contabilidaderc.com,']
    destinatarios_cc = ['fabio@contabilidaderc.com']
    #destinatarios_bcc = ['danielbessaribeiro@hotmail.com,danielbessaribeirouber@hotmail.com']

    try:
        # Criar a mensagem de e-mail
        msg = MIMEMultipart()
        msg['Subject'] = assunto
        msg['From'] = 'contabil03@contabilidaderc.com'  # Substitua pelo seu e-mail
        msg['To'] = ', '.join(destinatarios_principais)  # Define o(s) destinatário(s) principal(is)
        msg['Cc'] = ', '.join(destinatarios_cc)
        msg['Bcc'] = ','.join(destinatarios_bcc)
        # Adicionar o corpo do e-mail como HTML
        corpo = MIMEText(corpo_email, 'html', 'utf-8')
        msg.attach(corpo)

        # Conectar ao servidor SMTP
        s = smtplib.SMTP('mail.contabilidaderc.lan', 587)
        s.starttls()  # Inicializar a conexão TLS

        # Fazer o login
        password = 'Contabilidade123456@#*'  # Substitua pela sua senha
        s.login(msg['From'], password)

        # Enviar o e-mail com destinatários em To, CC e BCC
        destinatarios = destinatarios_principais + destinatarios_cc + destinatarios_bcc
        s.sendmail(msg['From'], destinatarios, msg.as_string())
        s.quit()

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Email enviado com sucesso!")

        # Fechar a janela do Tkinter após o sucesso
        root.quit()

    except Exception as e:
        # Exibir mensagem de erro usando Tkinter
        messagebox.showerror("Erro", f"Falha ao enviar o e-mail: {str(e)}")

# Configuração do Tkinter
root = Tk()
root.title("Envio de E-mail")

# Variáveis do Tkinter
mes_var = StringVar(root)
mes_var.set("Janeiro")  # Valor inicial do mês

tipo_email_var = StringVar(root)
tipo_email_var.set("EMAIL 1 - Antes do dia 10")  # Valor inicial do tipo de e-mail

# Lista de meses
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Lista de tipos de e-mail
tipos_email = ["EMAIL 1 - Antes do dia 10", "EMAIL 2 - Após o dia 10"]

# Widgets do Tkinter
label_mes = Label(root, text="Selecione o mês:")
label_mes.pack()

menu_mes = OptionMenu(root, mes_var, *meses)
menu_mes.pack()

label_tipo_email = Label(root, text="Selecione o tipo de e-mail:")
label_tipo_email.pack()

menu_tipo_email = OptionMenu(root, tipo_email_var, *tipos_email)
menu_tipo_email.pack()

botao_enviar = Button(root, text="Enviar", command=enviar_email)
botao_enviar.pack()

root.mainloop()
