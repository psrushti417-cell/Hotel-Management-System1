"""
URL configuration for hotal_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotelapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login_admin , name="Login_Admin"),
    path('SingUp_Guest/',views.SingUp_Guest , name="SingUp_Guest"),
    path('Login_Guest/', views.Login_Guest , name='Login_Guest'),
    path('Add_Guest/' , views.Add_Guest , name="Add_Guest"),
    path('Fogate_Password/' , views.Forget_password , name="Fogate_Password"),
    path('Update_Guest_Name/', views.Update_Guest_Name , name="Update_Guest_Name"),
    path('Delete_Guest/', views.Delete_Guest, name="Delete_Guest"),
    path('Show_All_Guests/',views.Show_All_Guests , name="Show_All_Guests"),
    path('Update_Guest_Address/',views.Update_Guest_Address , name="Update_Guest_Address"),
    path('Update_Guest_Mobail_Number/' , views.Update_Guest_Mobail_number , name="Update_Guest_Mobail_Number"),
    path('Update_Guest_Email_Id/' , views.Update_Guest_Email_Id , name="Update_Guest_Email_Id"),
    path('Show_Single_Guest/', views.Show_Guest_By_Id , name="Show_Single_Guest"),
    path('Guest_Crud/' , views.Guest_Crud , name="Guest_Crud"),
    
    # room urls
    
    path('Add_Room/' , views.Add_Room , name='Add_Room'),
    path('Delete_Room/' , views.Delete_Room , name='Delete_Room'),
    path('Show_All_Rooms/' , views.Show_All_Rooms , name='Show_All_Rooms'),
    path('Show_Single_Room/' , views.Show_Single_Room , name="Show_Single_Room"),
    path('Update_Room_Number/' , views.Update_Room_Number , name="Update_Room_Number"),
    path('Update_Room_Price/' , views.Update_Room_Price , name="Update_Room_Price"),
    path('Update_Room_Type/' , views.Update_Room_Type , name="Update_Room_Type"),
    path('Room_Crud/' , views.Room_Crud , name="Room_Crud"),
    
    #Booking Urls
    
    path('Add_Booking/' , views.Add_Booking , name="Add_Booking"),
    path('Delete_Booking/' , views.Delete_Booking , name="Delete_Booking"),
    path('Show_All_Bookings/' , views.Show_All_Booking , name="Show_All_Bookings"),
    path('Update_All_Data/' , views.Update_All_Data , name="Update_All_Data"),
    path('Update_Check_In_Out_And_Total_Days/' , views.Update_Check_in_out_Total_Days , name="Update_Check_In_Out_And_Total_Days"),
    # path('Update_Guest_Id_Number/' , views.Update_Guest_Id , name="Update_Guest_Id_Number"),
    path('Update_Room_Id_Number/' , views.Update_Room_Id , name="Update_Room_Id_Number"),
    path('Update_Booking_Status/' , views.Update_Status_Booking , name="Update_Booking_Status"),
    path('Show_Single_Booking/' , views.Show_Single_Booking , name="Show_Single_Booking"),
    path('Booking_Crud/' , views.Booking_Crud , name="Booking_Crud"),
    
    #Payment Urls
    path('Add_Payment/' , views.Add_Payment , name="Add_Payment"),
    path('Delete_Payment/' , views.Delete_Payment , name="Delete_Payament"),
    path('Show_All_Payments/' , views.Show_All_Payments , name="Show_All_Payments"),
    path('Show_Single_Payment/' , views.Show_Single_Payment , name="Show_Single_Payment"),
    
    
    #Admin urls
    
    path('Admin_Dashbord/' , views.Admin_Dashbord , name="Admin_Dashbord"),
    
    
]
