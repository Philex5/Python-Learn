"""
    一封电子邮件的旅程：
    发件人-> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
       -- MUA: Mail User Agent ——邮件客户代理       电子邮件软件
       -- MTA: Mail Transfer Agent ——邮件传输代理   Email提供商（网易、新浪等）
       -- MDA: Mail Delivery Agent ——邮件投递代理   服务器的数据库里即，电子邮箱
"""
"""
    编写程序发送和接收邮件实质是：
    ——编写MUA发送到MTA
    ——编写MUA从MDA收邮件

"""
"""
    发邮件时，MUA与MTA使用的协议是SMTP：Simple Mail Transfer Protocol
    收邮件，MUA与MDA使用的协议有：
        1. POP:Post Office Protocol,version3(POP3)
        2. IMAP:Internet Message Access Protocol version4(IMAP4):不仅可以收邮件，还可以操作MDA上的邮件 

"""