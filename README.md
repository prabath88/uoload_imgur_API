Docker Image Setup
------------------

1) Clone the Project to the Local PC.
   git clone https://prabath88@bitbucket.org/prabath88/prabath_challenge.git
   
2) Open the Project 
   cd prabath_challenge/
   
3) Run below command to Build the docker Image
   docker build -t flask-sample-one:latest .
   
4) Run the container from created image
   docker run -d -p 5081:5000 flask-sample-one
   
   note:- I gave 5080 for local PC port. you can specify the your own port. (not using)

Testing 
-------

  1) This is support only for the .jpg images

  sample request: (POST) http://127.0.0.1:5081/v1/images/upload
      
      {"urls":["http://www.nwiizone.com/wp-content/uploads/2006/11/Copia%20de%20Sonic_and_the_Secret_Rings_wii_04.jpg",
               "http://www.nwiizone.com/wp-content/uploads/2006/11/Copia%20de%20Sonic_and_the_Secret_Rings_wii_10.jpg",
               "http://www.nwiizone.com/wp-content/uploads/2006/11/Copia%20de%20Sonic_and_the_Secret_Rings_wii_09.jpg"
               ]
      }

  sample Output:
  
  {
    "JOBID": "2018-05-1319:25:29:UTC"
  }
    
  
  2) NOW Images ready to upload. To upload the images use below request 
  
     (GET) http://127.0.0.1:5081/v1/updatetoimgur 
     
     sample output:
      {
         "files Upload": "success...!"
      }
      
      
  3) To list down the uploaded images in your album use below request.
     
     (GET) http://13.232.13.238:5081/v1/images
     
     Sample Output:
     
     {
    "Uploaded": [
        "https://i.imgur.com/WVlEHO7.jpg",
        "https://i.imgur.com/G6jSrbS.jpg",
        "https://i.imgur.com/33a38b6.jpg",
        "https://i.imgur.com/nDEMyqK.jpg",
        "https://i.imgur.com/fFd5YCJ.jpg",
        "https://i.imgur.com/3Phq1VK.jpg",
        "https://i.imgur.com/qZ8HekZ.jpg",
        "https://i.imgur.com/ZZ8wa0Y.jpg",
        "https://i.imgur.com/bV3rWAJ.jpg",
        "https://i.imgur.com/HkrCUBZ.jpg",
        "https://i.imgur.com/vdMGjmP.jpg",
        "https://i.imgur.com/ceuwUpV.jpg",
       
     ]
    }
     
     
     
     
  
     
  
     