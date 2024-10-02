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

    destinatarios_bcc = [ 'destinatarios em copia oculta' ]
    destinatarios_principais = ['envio principal']
    destinatarios_cc = ['destinatarios em copia']

    try:
    
        msg = MIMEMultipart()
        msg['Subject'] = assunto
        msg['From'] = 'seu email' 
        msg['To'] = ', '.join(destinatarios_principais)  
        msg['Cc'] = ', '.join(destinatarios_cc)
        msg['Bcc'] = ','.join(destinatarios_bcc)
    
        corpo = MIMEText(corpo_email, 'html', 'utf-8')
        msg.attach(corpo)

     
        s = smtplib.SMTP('servidor do email', 587)
        s.starttls()  

      
        password = senha do email  
        s.login(msg['From'], password)

   
        destinatarios = destinatarios_principais + destinatarios_cc + destinatarios_bcc
        s.sendmail(msg['From'], destinatarios, msg.as_string())
        s.quit()

      
        messagebox.showinfo("Sucesso", "Email enviado com sucesso!")

        
        root.quit()

    except Exception as e:
     
        messagebox.showerror("Erro", f"Falha ao enviar o e-mail: {str(e)}")


root = Tk()
root.title("Envio de E-mail")


mes_var = StringVar(root)
mes_var.set("Janeiro") 

tipo_email_var = StringVar(root)
tipo_email_var.set("EMAIL 1 - Antes do dia 10") 


meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


tipos_email = ["EMAIL 1 - Antes do dia 10", "EMAIL 2 - Após o dia 10"]


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
