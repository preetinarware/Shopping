from django.shortcuts import render,redirect,HttpResponse
from home.models import More_Products,enquiries,mycart,Oders,profile,abouts,Book_testdrive,product_specif,product_access,product_key
from django.contrib import messages
from django.contrib.auth.models import User
#for login
from django.contrib.auth import authenticate,login,logout
#for send email
from django.core.mail import send_mail
from django.conf import settings
#for html to email
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

# Create your views here.
def home(request):
    index = More_Products.objects.all()
    res = {'title': index}
    return render(request,'home.html',res)

def product(request):
    index = More_Products.objects.all()
    res = {'title': index}
    return render(request,'product_page.html',res)

def about(request):
    page=abouts.objects.all()
    deatil={'tite':page}
    return render(request,'about.html',deatil)

def contact(request):
     if request.method=="POST":
          print(request.method)
        #send_mail(subject, message, configuredemail, reciver, fail_silently)
          name =request.POST['name']
          email = request.POST['email']
          contact_no= request.POST['contact_no']
          subject = request.POST['subject']
          your_ques = request.POST['your_ques']
          var = enquiries(name=name,email=email, contact_no=contact_no,subject=subject,your_ques=your_ques)
          var.save()
          print(var)
          data={'name':name,
                'email':email,
                'contact_no':contact_no,
                "subject":subject,
                'your_ques':your_ques}
          #print(data)
          deatil = {'tite':data}
         # print(deatil)
          html_content = render_to_string('mailpage.html',deatil)
         # print(html_content)
          text = strip_tags(html_content)
         # print(text)
          send_mail('for enqury', text, email, ['narware0422@gmail.com'])
          messages.success(request, "mail send successfully ")
          return redirect('contact')

     return render(request,'contact.html')
def profile_edit(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            image = request.POST['image']
            contact = request.POST['contact']
            gender = request.POST['gender']
            DOB = request.POST['DOB']
            Current_add = request.POST['Current_add']
            Permanant_add = request.POST['Permanant_add']
            # var =profile(username=username, image=image, DOB= DOB,Permanant_add=Permanant_add,
            #               contact=contact,  gender= gender,  Current_add= Current_add,user_ids=request.user.id)
            blogid=request.GET.get('blogid')
            # print(blogid)
            usr=profile.objects.filter(user_ids=request.user.id)
            # print('usrrrrrrrr',usr)
            if len(usr)>0:
                ob=usr[0]
                ob.username=username
                ob.image = image
                ob.DOB = DOB
                ob.Permanant_add = Permanant_add
                ob.contact=contact
                ob.gender= gender
                ob.Current_add = Current_add
                # print(ob.username,ob.gender,ob.DOB,ob.Permanant_add,ob.contact,ob.Current_add,ob.image)
                ob.save()
                # print('ooo', ob)
            else:
                var = profile(username=username, image=image, DOB=DOB, Permanant_add=Permanant_add,
                              contact=contact, gender=gender, Current_add=Current_add, user_ids=request.user.id)
                var.save()
        redirect('myprofile')
        messages.success(request, "Profile updated successfully ")
    return render(request, 'profile_editing.html')
def myprofile(request):
     if request.user.is_authenticated:
        data=profile.objects.filter(user_ids=request.user.id)
        # print('filterdata',data)
        if len(data)>0:
            obb=data[0]
            # print('obb',obb)
            datas=profile.objects.get(user_ids=request.user.id)
            # print(('get data',datas))
            obb.data=datas
            # print(('obb.data',obb.data))
            obb.save()
        res = {'title':data}
        # print(res)
     return render(request,'Profile.html',res)
def myorder(request):
         index = Oders.objects.all()
         ress = {'tit': index}
         print('ress',ress)
         return redirect('myprofile')
def prod_link(request):
    blogid = request.GET.get('blogid')
    print(blogid)
    index = Oders.objects.get(id=blogid)
    print(index.pincode)
    ress = {'title': index}
    print('rrrr',ress)
    return render(request, 'product_link.html', ress)
def testdrives(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        zipcode = request.POST['zipcode']
        Bike_model=request.POST['Bike_model']
        Addres=request.POST['Addres']
        your_question = request.POST['your_question']
        cap = Book_testdrive(name=name, email=email, contact_no=contact_no,Addres=Addres, zipcode=zipcode,Bike_model=Bike_model, your_question=your_question)
        cap.save()
        data = {'name': name,   'email': email,
                'contact_no': contact_no,
                "Addres": Addres, 'zipcode':zipcode,
                'Bike_model':Bike_model,'your_question':your_question}
        deatil = {'tite': data}
        html_content = render_to_string('testdrive.html', deatil)
        text = strip_tags(html_content)
        send_mail('Book Test Drive', text, email, ['narware0422@gmail.com'])
        messages.success(request, "mail send successfully ")
    return render(request,'testdrive.html')
def Details(request):
    blogid = request.GET.get('blogid')
    #print(blogid)
    index = More_Products.objects.get(id=blogid)
    specs = product_access.objects.filter(prod_id=blogid)
    access = product_specif.objects.filter(prod_id=blogid)
    keys = product_key.objects.filter(prod_id=blogid)
    res = {'title': index,'specs':specs,'access':access,'key':keys}
    return render(request,'ProductDetails.html',res)
def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password= request.POST['password']
        confirm = request.POST['confirm']
        fname = request.POST['fname']
        lname = request.POST['lname']
        user=User.objects.create_user(username=name,email=email,password=password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        if user is None:
            messages.error(request, "invalid entry")
            return redirect('home')
        else:
            messages.success(request,"Your account has been successfully created")
            return redirect('home')
    return render(request,'Register.html')
def handlelogin(request):
    if request.method=='POST':
         loginemail = request.POST['loginemail']
         username = User.objects.get(email=loginemail).username
         pass1 = request.POST['pass1']
         user= authenticate(username=username,password=pass1)
         if user is not None:
            login(request,user)
            if not request.user.is_authenticated:
               messages.success(request, 'user none')
               return redirect('login')
            else:
                messages.success(request, 'successfully logged In')
                return redirect('myprofile')
         messages.error(request, 'Invalid user')
         return redirect('home')
    return render(request,'user_login.html')
def handlelogout(request):
    logout(request)
    messages.success(request, 'successfully logged Out')
    return redirect('home')
def cart(request):
    cartitems=mycart.objects.filter(user=request.user.id)
    print(cartitems)
    li = []
    res={}
    total = 0
    for data in cartitems:
        print(data)
        prodidd = data.product_id
        print(prodidd)
        prod = More_Products.objects.get(id=prodidd)
        print(prod)
        price = prod.price * data.quntity
        print(price)
        total += price
        li.append([prod,data.quntity,price])
        res={'cartlist':li,'totle':total}
        print(res)
    return render(request,'Cart.html',res)
def add_to_cart(request):
     if request.user.is_authenticated:
         blogid = request.GET.get('blogid')
         #print(blogid)
         checkprod = mycart.objects.filter(user=request.user.id,product_id=blogid)
         # print(checkprod)
         if len(checkprod) > 0:
             ob = checkprod[0]
             ob.quntity += 1
             ob.save()
         else:
            index = mycart(user=request.user.id, product_id=blogid, quntity=1)
            index.save()
     return redirect('cart')
def remove_from_cart(request):
    blogid = request.GET.get('blogid')
   # print(blogid)
    item = mycart.objects.filter(user=request.user.id, product_id=blogid)
    #print(item)
    if len(item) > 0:
        ob = item[0]
        if ob.quntity!=1:
            ob.quntity -= 1
            ob.delete()
    return redirect('cart')
def increase(request):
    blogid = request.GET.get('blogid')
    #print(blogid)
    itemlist = mycart.objects.filter(user=request.user.id, product_id=blogid)
    #print(itemlist)
    if len(itemlist) > 0:
        ob = itemlist[0]
        if ob.quntity != 0:
            ob.quntity += 1
            ob.save()

    return redirect('cart')
def decrease(request):
    blogid = request.GET.get('blogid')
    #print(blogid)
    itemlist = mycart.objects.filter(user=request.user.id, product_id=blogid)
    #print(itemlist)
    if len(itemlist) > 0:
        ob = itemlist[0]
        if ob.quntity!=0:
            ob.quntity -= 1
            ob.save()
        else:
            ob.delete()
    return redirect('cart')
def checkout(request):
    items = mycart.objects.filter(user=request.user.id)
    lis = []
    ress = {}
    totals = 0
    for datas in items:
        prodids = datas.product_id
        prods = More_Products.objects.get(id=prodids)
        # print(data.quntity)
        #print(prodids)
        prices = prods.price * datas.quntity
        totals += prices
        lis.append([prods, datas.quntity, prices])
        ress = {'list': lis, 'totl': totals}
    return render(request, 'check.html', ress)

def place(request):
    lists=[]
    resd={}
    items = mycart.objects.filter(user=request.user.id)
    totals = 0
    for datas in items:
        prodidss = datas.product_id
        prods = More_Products.objects.get(id=prodidss)
        itemname = More_Products.objects.get(id=prodidss).name
        prices = prods.price * datas.quntity
        totals += prices
        lists.append([prods, datas.quntity, prices])

        if request.method == "POST":
           name = request.POST['name']
           contact_no = request.POST['contact_no']
           addres1 = request.POST['addres1']
           addres2 = request.POST['addres2']
           pincode = request.POST['pincode']
           var = Oders(name=name,product_name=itemname,prodid=prodidss,contact_no=contact_no,addres1=addres1,addres2=addres2,
                        pincode=pincode,total=totals,quntitys=datas.quntity,price=prices)
           var.save()
           datas.delete()
           messages.success(request, 'Order placed successfully ')
    return redirect('cart')
    # return render(request, 'check.html')
