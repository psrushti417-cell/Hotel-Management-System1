from django.shortcuts import render , redirect
from email import message
from urllib import request
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .models import Guest , Room , Payment , Booking 
from datetime import datetime

# Create your views here.

def Login_admin(request):
    error = ""
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        
            User = authenticate(request,username = username , password = password)
        
            if User is not None:
                login(request,User)
                return redirect('Admin_Dashbord')
            else:
                error = "Enter a valid Usename And Password"
    except:
            error = "enter a valid Usename And Password"
            
    return render(request, 'login/loginadmin.html',{ 'error':error})

# Guest All Functions Is Above

def SingUp_Guest(request):
    error = ""
    if request.method == "POST":
        try:
            Guest.objects.create(
                gid = request.POST.get('gid'),
                gname = request.POST.get('gname'),
                gemail = request.POST.get('gemail'),
                gmob_no = request.POST.get('gmob_no'),
                gid_proof = request.POST.get('gid_proof'),
                address = request.POST.get('address'),
                gl_password = request.POST.get('gl_password')
            )
            return HttpResponse("Singup sucessfully")
        except:
            error = "You Have all ready an account"
    
    
    return render(request, 'login/singup_guest.html',{'error':error})

def Login_Guest(request):
    error = ''
    if request.method == "POST":
        gid_proof = request.POST.get('gid_proof')
        gl_password = request.POST.get('gl_password')
        
        try:
            login_guest = Guest.objects.get(gid_proof = gid_proof,gl_password = gl_password)
            return redirect('Guest_Crud')
        except :
            error = "enter a currect id proof and password"
    return render(request, 'login/Login_Guest.html',{'error': error})

def Forget_password(request):
    error = ''
    message = ''
    if request.method == "POST":
        gid_proof = request.POST.get('gid_proof')
        
        try:
            g = Guest.objects.get(gid_proof = gid_proof)
            g.gl_password = request.POST.get('gl_password')
            g.save()
            
            message = "Password update sucessfully"
        except:
            error = "usesr is not found"
            
    return render(request , 'login/forgetguestpasssward.html',{'error':error , 'message' :message})

def Add_Guest(request):
    error = ""
    msg = ""
    if request.method == "POST":
        try:
            Guest.objects.create(
                gid = request.POST.get('gid'),
                gname = request.POST.get('gname'),
                gemail = request.POST.get('gemail'),
                gmob_no = request.POST.get('gmob_no'),
                gid_proof = request.POST.get('gid_proof'),
                address = request.POST.get('address'),
                gl_password = request.POST.get('gl_password')
            )
            msg = "Add sucess fullay"
        except:
            error = "You Have all ready an account"
    
    
    return render(request, 'Guest/addguest.html',{'error':error , 'msg' : msg})

def Delete_Guest(request):
    message = ''
    error = ''
    if request.method == "POST":
        gid = request.POST.get('gid')
        
        try:
            user_delete = Guest.objects.get(gid=gid)
            user_delete.delete()
            message = f"Delate sucessfullay user id {gid}"
        except :
            error = f"{gid} no user not found"
    return render(request, 'Guest/deleteguest.html',{'error':error , 'message':message})

def Update_Guest_Name(request):
    error = ''
    message = ''
    if request.method == "POST":
        gid = request.POST.get('gid')
    
        try:
            g = Guest.objects.get(gid = gid)
            g.gname = request.POST.get('gname')
            g.save()
            message = f"update guest name of id number {gid}"
        except:
            error=f"not found user for user number {gid}"
    return render(request,'Guest/updateguestname.html',{'error': error , 'message' : message})

def Update_Guest_Address(request):
    error = ''
    message = ''
    
    if request.method == "POST":
        gid = request.POST.get('gid')
        
        try:
            g = Guest.objects.get(gid=gid)
            g.address = request.POST.get('address')
            g.save()
            message = f"g id no {gid} address is updated"
        except :
            error = f"{gid} no user is not found"
    return render(request, 'Guest/updateguestaddress.html',{'error':error,'message':message})

def Update_Guest_Mobail_number(request):
    error = ''
    message = ''
    error1 = ''
    
    if request.method == "POST":
        gid = request.POST.get('gid')
        gmob_no = request.POST.get('gmob_no')
        
        try:
            if len(gmob_no) <= 9 or len(gmob_no) >=11:
                error = f"please enter a 10 digit mobail number "
            else:
                g = Guest.objects.get(gid = gid)
                g.gmob_no = request.POST.get('gmob_no')
                g.save()
                message = f"{gmob_no} is updated sucessfullay"
        except :
            error1=f"{gid} number uder id not found"
    return render(request, 'Guest/updateguestmobailno.html' , {"error":error , "message" : message , "error1" : error1})

def Update_Guest_Email_Id(request):
    error = ''
    message = ''
    allreadyemail =''
    
    if request.method == "POST":
        gid = request.POST.get('gid')
        gemail = request.POST.get('gemail')
        
        
        try:
            if Guest.objects.filter(gemail = gemail).exists():
                allreadyemail = f"{gemail} is all ready exist enter another enail id"
            else:
                g = Guest.objects.get(gid = gid)
                g.gemail = request.POST.get('gemail')
                g.save()
            
                message = f'{g.gemail} id update sucessfullay!'
        
        except:
            error = f"{gid} no guest not found"
            
    return render(request, 'Guest/updateguestemailid.html' , {"error":error , "message" : message, "allreadyemail" : allreadyemail}  )

            
def Show_All_Guests(request):
    guests = Guest.objects.all()
    return render(request, 'Guest/showallguest.html' , {'guests':guests})

def Show_Guest_By_Id(request):
    error = ''
    g = None
    
    if request.method == "POST":
        gid = request.POST.get('gid')
        
        try:
            g = Guest.objects.filter(gid = gid).first()
        except:
            error=f"{gid} user is not found"
    return render(request, 'Guest/viewguest.html' , {"error" : error,"g": g})

def Guest_Crud(request):
    return render(request, 'Guest/guestcrud.html')


    
# Room All Functions Is Above

def Add_Room(request):
    error = ''
    message = ''

    if request.method == "POST":
        try:
            Room.objects.create(
                rid = request.POST.get('rid'),
                room_no = request.POST.get('room_no'),
                room_type = request.POST.get('room_type'),
                price_per_day = request.POST.get('price_per_day'),
            )
            message = 'Add sucessfullay'
        except:
            error = "Please enter a valid data"    
        
    return render(request, 'Room/addroom.html' , {"message" : message , "error" : error})

def Delete_Room(request):
    error = ""
    message = ""
    
    if request.method == "POST":
        rid = request.POST.get('rid')
        
        try:
            
            d = Room.objects.get(rid = rid)
            d.delete()
            message = "Delete Sucessfulaly"
        
        except:
            error = "User not found "
            
    return render(request, 'Room/deleteroom.html' , {"error" : error , "message" : message})

def Show_All_Rooms(request):
    rooms = Room.objects.all()
    return render(request, 'Room/showallroom.html' , {'rooms' : rooms})

def Show_Single_Room(request):
    r = None
    if request. method == "POST":
        room_type = request.POST.get('room_type')
        
        r = Room.objects.filter(room_type = room_type).first()
        
    return render(request, 'Room/viewroom.html' , {"r" : r})

def Update_Room_Number(request):
    error = ''
    message = ""
    
    if request.method == "POST":
        rid = request.POST.get('rid')
        
        try:
            
            r = Room.objects.get(rid = rid )
            r.room_no = request.POST.get('room_no')
            r.save()
            
            message = "room number is update sucessfully"
            
        except:
            
            error = "room not found"
    
    return render(request, 'Room/updateroomnu.html' , {'error' : error, 'message' : message})

def Update_Room_Price(request):
    error = ""
    message = ""
    
    if request.method == "POST":
        rid = request.POST.get('rid')
        
        try:
            
            r = Room.objects.get(rid = rid)
            r.price_per_day = request.POST.get('price_per_day')
            r.save()
            
            message = "room prize is updated sucessfully"
            
        except:
            
            error = "Room is not found"
        
    return render(request, 'Room/updateroomprize.html' ,{"error" : error , "message" : message})

def Update_Room_Type(request):
    error = ""
    message =""
    
    if request.method == "POST":
        rid =request.POST.get('rid')
        
        try:
            
            r = Room.objects.get(rid = rid)
            r.room_type = request.POST.get('room_type')
            r.save()
            
            message = 'Room Type update sucessfully'
            
        except:
            
            error = "user not found"
            
    return render(request, 'Room/updateroomtype.html' , {"error" : error , "message" : message})

def Room_Crud(request):
    return render(request, 'Room/roomcrud.html')

#Booking Functions

from datetime import datetime
from django.shortcuts import render
from .models import Booking, Guest, Room

def Add_Booking(request):

    guests = Guest.objects.all()
    rooms = Room.objects.all()

    if request.method == "POST":
        bid = request.POST.get("bid")
        gid = request.POST.get("gid")
        rid = request.POST.get("rid")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        status = request.POST.get("status")

        # Booking ID check
        if Booking.objects.filter(bid=bid).exists():
            return render(request, "Booking/addbooking.html", {
                "error": "Booking ID already exists",
                "guests": guests,
                "rooms": rooms
            })

        # Get Guest
        try:
            guest = Guest.objects.get(pk=gid)
        except Guest.DoesNotExist:
            return render(request, "Booking/addbooking.html", {
                "error": "Guest not found",
                "guests": guests,
                "rooms": rooms
            })

        # Get Room
        try:
            room = Room.objects.get(pk=rid)
        except Room.DoesNotExist:
            return render(request, "Booking/addbooking.html", {
                "error": "Room not found",
                "guests": guests,
                "rooms": rooms
            })

        # Date Validation
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()
        except:
            return render(request, "Booking/addbooking.html", {
                "error": "Invalid date format",
                "guests": guests,
                "rooms": rooms
            })

        if check_out_date <= check_in_date:
            return render(request, "Booking/addbooking.html", {
                "error": "Check-out must be after check-in",
                "guests": guests,
                "rooms": rooms
            })

        # Room availability check
        overlapping = Booking.objects.filter(
            rid=room,
            check_in__lt=check_out_date,
            check_out__gt=check_in_date
        ).exists()

        if overlapping:
            return render(request, "Booking/addbooking.html", {
                "error": "Room already booked for selected dates",
                "guests": guests,
                "rooms": rooms
            })

        total_days = (check_out_date - check_in_date).days

        if not status:
            status = "Booked"

        Booking.objects.create(
            bid=bid,
            gid=guest,
            rid=room,
            check_in=check_in_date,
            check_out=check_out_date,
            total_day=total_days,
            status=status
        )

        return render(request, "Booking/addbooking.html", {
            "message": "Booking added successfully 🎉",
            "guests": guests,
            "rooms": rooms
        })

    return render(request, "Booking/addbooking.html", {
        "guests": guests,
        "rooms": rooms
    })

def Delete_Booking(request):
    
    error = ""
    message = ""
    
    if request.method == "POST":
        bid = request.POST.get('bid')
        
        try:
            
            delete_booking = Booking.objects.get(bid = bid )
            delete_booking.delete()
            message = "Deleted Sucessfully"
            
        except:
            
            error = "Booking is not found"
            
    return render(request , 'Booking/deletebooking.html' , {"error" : error , "message" : message})

def Show_All_Booking(request):
    bookings = Booking.objects.all()
    return render(request, 'Booking/showallbooking.html' , {"bookings" : bookings})

from datetime import datetime
from django.shortcuts import render, HttpResponse
from .models import Booking, Guest, Room

def Update_All_Data(request):

    error = ""
    message = ""

    guests = Guest.objects.all()
    rooms = Room.objects.all()

    if request.method == "POST":

        bid = request.POST.get("bid")
        gid = request.POST.get("gid")
        rid = request.POST.get("rid")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        status = request.POST.get("status")

        # -------- Booking Validation --------
        try:
            booking = Booking.objects.get(bid=bid)
        except Booking.DoesNotExist:
            return render(request, 'Booking/updatealldata.html', {
                "error": "Booking not found",
                "guests": guests,
                "rooms": rooms
            })

        # -------- Guest Validation --------
        try:
            guest = Guest.objects.get(gid=int(gid))
        except:
            return render(request, 'Booking/updatealldata.html', {
                "error": "Guest ID does not exist",
                "guests": guests,
                "rooms": rooms,
                "b": booking
            })

        # -------- Room Validation --------
        try:
            room = Room.objects.get(rid=int(rid))
        except:
            return render(request, 'Booking/updatealldata.html', {
                "error": "Room ID does not exist",
                "guests": guests,
                "rooms": rooms,
                "b": booking
            })

        # -------- Date Validation --------
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()
        except:
            return render(request, 'Booking/updatealldata.html', {
                "error": "Invalid date format",
                "guests": guests,
                "rooms": rooms,
                "b": booking
            })

        if check_out_date <= check_in_date:
            return render(request, 'Booking/updatealldata.html', {
                "error": "Check-out must be after check-in",
                "guests": guests,
                "rooms": rooms,
                "b": booking
            })

        # -------- Overlapping Check --------
        overlapping = Booking.objects.filter(
            rid=room,
            check_in__lt=check_out_date,
            check_out__gt=check_in_date
        ).exclude(bid=bid).exists()

        if overlapping:
            return render(request, 'Booking/updatealldata.html', {
                "error": "Room already booked for selected dates",
                "guests": guests,
                "rooms": rooms,
                "b": booking
            })

        # -------- Update Booking --------
        booking.gid = guest
        booking.rid = room
        booking.check_in = check_in_date
        booking.check_out = check_out_date
        booking.total_day = (check_out_date - check_in_date).days
        booking.status = status if status else "Booked"
        booking.save()

        message = "Booking updated successfully 🎉"

        return render(request, 'Booking/updatealldata.html', {
            "message": message,
            "guests": guests,
            "rooms": rooms,
            "b": booking
        })

    return render(request, 'Booking/updatealldata.html', {
        "guests": guests,
        "rooms": rooms
    })

def Update_Check_in_out_Total_Days(request):
    
    error1 = ""
    message = ""
    
    if request.method == "POST":
        bid = request.POST.get('bid')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        total_day = request.POST.get('total_day')
        
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()
        except:
            error1 = "Invalid date format"
            return render(request, 'Booking/updatealldata.html', locals())
        
        calculate_total_days = (check_out_date - check_in_date).days
        
        if check_out_date <= check_in_date:
            error1 = f"you are enter a old date from {check_in}"
            
            
        elif int(total_day) != calculate_total_days:
            error1 = f"total days = {calculate_total_days}"
            
        
        else:
            try:
                b = Booking.objects.get(bid = bid)
                b.check_in = request.POST.get('check_in')
                b.check_out = request.POST.get('check_out')
                b.total_day = request.POST.get('total_day')
                b.save()

                message = "data is updates sucessfullay 1"
            except:
                error1 = "Booking is not found"
        
    
    return render(request, 'Booking/updatecheckout_in_total.html' ,{"error1" : error1 , "message" : message})
from datetime import datetime
from django.shortcuts import render
from .models import Booking, Guest, Room

def Booking_Update_All(request):
    """
    Single view to handle:
    - Full booking update
    - Guest ID update
    - Room ID update
    - Dates update
    - Status update
    """

    error = ""
    message = ""

    guests = Guest.objects.all()
    rooms = Room.objects.all()
    b = None  # default booking object

    if request.method == "POST":
        bid = request.POST.get("bid")
        gid = request.POST.get("gid")
        rid = request.POST.get("rid")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        status = request.POST.get("status")

        # -------- Booking Validation --------
        try:
            b = Booking.objects.get(bid=int(bid))
        except ValueError:
            error = "Invalid Booking ID"
            return render(request, "Booking/updatealldata.html", locals())
        except Booking.DoesNotExist:
            error = "Booking not found"
            return render(request, "Booking/updatealldata.html", locals())

        # -------- Guest Validation --------
        if gid:
            try:
                guest = Guest.objects.get(gid=int(gid))
                b.gid = guest
            except ValueError:
                error = "Invalid Guest ID"
                return render(request, "Booking/updatealldata.html", locals())
            except Guest.DoesNotExist:
                error = "Guest not found"
                return render(request, "Booking/updatealldata.html", locals())

        # -------- Room Validation --------
        if rid:
            try:
                room = Room.objects.get(rid=int(rid))
            except ValueError:
                error = "Invalid Room ID"
                return render(request, "Booking/updatealldata.html", locals())
            except Room.DoesNotExist:
                error = "Room not found"
                return render(request, "Booking/updatealldata.html", locals())

        # -------- Date Validation --------
        if check_in and check_out:
            try:
                check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
                check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()
            except:
                error = "Invalid date format"
                return render(request, "Booking/updatealldata.html", locals())

            if check_out_date <= check_in_date:
                error = "Check-out must be after check-in"
                return render(request, "Booking/updatealldata.html", locals())

            # Overlapping check
            overlapping = Booking.objects.filter(
                rid=b.rid if not rid else room,
                check_in__lt=check_out_date,
                check_out__gt=check_in_date
            ).exclude(bid=b.bid).exists()

            if overlapping:
                error = "Room already booked for selected dates"
                return render(request, "Booking/updatealldata.html", locals())

            b.check_in = check_in_date
            b.check_out = check_out_date
            b.total_day = (check_out_date - check_in_date).days

        # -------- Status Update --------
        if status:
            b.status = status

        b.save()
        message = "Booking updated successfully 🎉"

    return render(request, "Booking/updatealldata.html", {
        "guests": guests,
        "rooms": rooms,
        "b": b,
        "error": error,
        "message": message
    })

    
def Update_Room_Id(request):
    
    error = ""
    message = ""

    if request.method == "POST":

        bid = request.POST.get('bid')
        rid = request.POST.get('rid')

        # ---------- Basic validation ----------
        if not bid or not rid:
            error = "Booking ID and Guest ID are required"
            return render(request, 'Booking/updateridno.html', {"error": error})

        # ---------- Guest validation ----------
        try:
            room = Room.objects.get(rid=int(rid))   # 🔥 SAFE
        except Room.DoesNotExist:
            error = "Guest not found"
            return render(request, 'Booking/updateridno.html', {"error": error})
        except ValueError:
            error = "Invalid Guest ID"
            return render(request, 'Booking/updateridno.html', {"error": error})

        # ---------- Booking validation ----------
        try:
            booking = Booking.objects.get(bid=bid)
        except Booking.DoesNotExist:
            error = "Booking not found"
            return render(request, 'Booking/updateridno.html', {"error": error})

        # ---------- Update ----------
        booking.rid = room
        booking.save()

        message = "Guest ID successfully updated 🎉"

    return render(request, 'Booking/updateridno.html',
                {"error": error, "message": message})
    
def Update_Status_Booking(request):
    
    error = "" 
    message = ""
    
    if request.method == "POST":
        bid = request.POST.get("bid")
        
        try:
            
            b = Booking.objects.get(bid = bid)
            b.status = request.POST.get("status")
            b.save()
            
            message = "Updates sucessfullay"
        
        except:
            
            error = "Booking is not found"
    
    return render(request , 'Booking/updatestatus.html' , {'error' : error , 'message' : message})

def Show_Single_Booking(request):
    
    error = ""
    message = ""
    b = None
    
    if request.method == "POST":
        bid = request.POST.get('bid')
        
        try:
            
            b = Booking.objects.filter(bid = bid).first()
        
        except:
            
            error = "Bookin is not found"
            
    return render(request, 'Booking/viewbooking.html' , {"error" : error , "message" : message , "b" : b})

def Booking_Crud(request):
    return render(request, 'Booking/bookingcrud.html')


#Payment all Functions



# views.py
from django.shortcuts import render
from .models import Booking, Room, Payment

def Add_Payment(request):
    error = ""
    message = ""
    check_in_date = ""
    check_out_date = ""
    amounts = 0

    if request.method == "POST":
        try:
            pid = request.POST.get('pid')
            bid = request.POST.get('bid')
            rid = request.POST.get('rid')
            payment_date = request.POST.get('payment_date')
            payment_mode = request.POST.get('payment_mode')
            paid = request.POST.get('paid')

            # Get Booking and Room
            booking = Booking.objects.get(pk=bid)
            room = Room.objects.get(pk=rid)

            # Fill check-in/out for display
            check_in_date = booking.check_in
            check_out_date = booking.check_out

            # Calculate total amount
            total_days = (check_out_date - check_in_date).days
            amounts = total_days * room.price_per_day

            # Save Payment
            Payment.objects.create(
                pid=pid,
                bid=booking,
                rid=room,
                amount=amounts,
                payment_mode=payment_mode,
                paid=paid,
                payment_date=payment_date
            )

            message = "Payment added successfully!"

        except Booking.DoesNotExist:
            error = "Booking ID not found."
        except Room.DoesNotExist:
            error = "Room ID not found."
        except Exception as e:
            error = f"An error occurred: {str(e)}"

    context = {
        "error": error,
        "message": message,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date,
        "amounts": amounts
    }

    return render(request, 'Payment/addpayment.html', context)

def Delete_Payment(request):
    
    error = ""
    message = ""
    
    if request.method == "POST":
        pid = request.POST.get('pid')
        
        try:
            
            d = Payment.objects.get(pid = pid)
            d.delete()
            
            message = "deleted sucessfullay"
        except:
            
            error = "Payment id not found"
        
    return render(request, 'Payment/deletepayment.html' , {"error" : error , "message" : message})

def Show_All_Payments(request):
    payments = Payment.objects.all()
    return render(request , 'Payment/showpayment.html' , {"payments" : payments})

def Show_Single_Payment(request):
    
    error = ""
    message = ''
    p=None
    
    if request.method == "POST":
        pid = request.POST.get('pid')
        
        try:
            
            p = Payment.objects.filter(pid = pid).first()
            
        except:
            
            error = "User not found"
            
    return render(request , 'Payment/viewpayment.html' , {"p" : p})
            

#Admin Functions

def Admin_Dashbord(request):
    return render(request , 'Admin/admindashbord.html')