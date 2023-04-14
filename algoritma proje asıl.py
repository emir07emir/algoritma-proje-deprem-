print("----------------------uygulamamıza hoşgeldiniz---------------------------\n")

username="iemirerdogan07"
password="abc123"




#--> üye olma kısmı
check=input("üye oldunuz mu?:")
if check=="hayır":
    username=input("kullanıcı adını oluşturunuz:")
    password=input("şifre oluşturunuz:")
    print("başarıyla üye olunmuştur")
elif check=="evet":    
    print("giriş yapma kısmına geçiniz")


#--> giriş yapma kısmı
   
while True:
     kullaniciadi=input("kullanıcı adınızı giriniz:")
     if kullaniciadi==username:
          print("kullanıcı adınız doğrudur")
          break
     else:
          print("kullanıcı adınız yanlıştır bir daha deneyin")
          continue
    
#-->şifremi unuttum kısmı
kontrol=input("şifrenizi unuttunuz mu?:")
if kontrol=="evet":
    password=(input("şifrenizi oluşturunuz:"))
    print("şifreniz oluşturuldu")


while True:
     
      sifre=input("şifrenizi giriniz:")
      if sifre==password:
          print("şifreniz doğrudur")
          print("uygulamaya giriş yapılmıştır")
          break
      else:
          print("şifreniz yanlıştır tekrar deneyin")
          continue
          

          


      
        
      