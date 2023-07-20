from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .models import Gallery
fs = FileSystemStorage()

# Create your views here.
def home(request):
    gallery = Gallery.objects.all()
    return render(request,"multipleimagesapp/home.html",{"context":gallery})

def uploadhandler(request):
    if request.method == "POST":
        images_id = request.POST.get("image_id")
       
        print("---------------->", images_id)
        if images_id:
            print("------------")
            gallery_instance = Gallery.objects.get(pk=images_id)
        else:
            print("i am running")
            title = request.POST.get('title')
            gallery_instance = Gallery.objects.create(title=title)
                
        
        files = request.FILES.getlist('images')
        if files:
            # gallery_instance = Gallery.objects.create(title=title)

            for count,file in enumerate(files):
                try:
                    # new_name = str(gallery_instance.pk) +"-"+ file.name
                    # print(file.name, new_name)
                    saved_file_instance = fs.save(file.name,file)
                except Exception as e:
                    print(f"Exception : {e}")
                else:
                    
                    image_field = gallery_instance.images
                    if images_id and image_field and count == 0: # its update request and image field is not empty
                        image_field =  image_field +','+ fs.url(saved_file_instance)
                    else:
                        image_field =  image_field + fs.url(saved_file_instance)

                    if count < len(files)-1:
                        image_field = image_field + ","
                    gallery_instance.images = image_field
                    gallery_instance.save()

    return redirect(reverse("multipleimagesapp:home"))

def gallery(request,pk):
    gallery_instance = Gallery.objects.filter(pk=pk)
    data = dict()
    
    if gallery_instance:
        # print("running", gallery_instance)
        data["title"] = gallery_instance[0].title
        if gallery_instance[0].images:
            data["images"] = gallery_instance[0].images.split(",")
        # print(data)
        return render(request, "multipleimagesapp/gallery.html",{'data_uid':pk, "data":data})
    message = "Either instance not exist or wrong request made"
    return redirect(reverse("multipleimagesapp:home"))

def delete(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        file_name = request.POST["image"]
        gallery_instance = Gallery.objects.filter(pk=uid)
        print("running delete",gallery_instance)
        if gallery_instance:
            print("running if")
            try:
                file_name_delete =file_name

                if gallery_instance[0].images.split(",")[-1] == file_name:
                    if len(gallery_instance[0].images.split(","))!=1:
                        file_name_delete = ","+file_name_delete 
                else:
                    print("not at end")
                    file_name_delete = file_name_delete + ","
                    print("file name to del", file_name_delete)
                gallery_instance[0].images = gallery_instance[0].images.replace(file_name_delete,"")
                gallery_instance[0].save()
                print(file_name)
                print("images",gallery_instance[0].images)
            except Exception as e:
                print(f"Exception : {e}")
            else:
                file_name = file_name.split("/")[-1]
                file_name = file_name.replace("%20"," ")
                print(file_name,type(file_name))
                print("------------------>",file_name)
                try:
                    pass
                    fs.delete(file_name)
                except Exception as e:
                    print("------------------------")
                    print(e)
                # print("sadas0",file_name.split("/")[-1])
                print("---------------")
        return redirect(reverse('multipleimagesapp:gallery',args=(uid,)))
    return redirect(reverse("multipleimagesapp:home"))

def update(request):
    if request.method == "POST":
        uid = request.POST['uid']
        image = request.POST['image']
        file = request.FILES['file']
        try:
            gallery_instance = Gallery.objects.get(pk =uid)
            saved_file_instance = fs.save(file.name,file)
            gallery_instance.images = gallery_instance.images.replace(image,fs.url(saved_file_instance))
        except Exception as e:
            print(e)
        else:
            gallery_instance.save()
            file_name = image.split("/")[-1]
            file_name = file_name.replace("%20"," ")
            fs.delete(file_name)
        return redirect(reverse('multipleimagesapp:gallery',args=(uid,)))
    return redirect(reverse("multipleimagesapp:home"))

def extend(request):
    pass