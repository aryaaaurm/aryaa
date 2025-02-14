#from flask import Flask, request, jsonify
# user_data ={ #user_data (json file)
#         "user_id":"still has to given", #used to access function parameter that was entered by user
#         "name": "aryaa",
#         "email":"aruaaa123@gmail.com"
#     }
#app = Flask(__name__)

#@app.route("/",methods=["GET"])
#def welcome():
 #   print("yuegfuigeiufgeufh") 
  #  return "welcome to my api"

#@app.route("/user",methods=["GET"])# user id is smth we need to enter in order 
#to get or call a value from the file that user requested
#def get_user(): #function used for route and access userid for get
    # user_data ={ #user_data (json file)
    #     "user_id":user_id, #used to access function parameter that was entered by user
    #     "name": "aryaa",
    #     "email":"aruaaa123@gmail.com"
    # }

    # extra = request.args.get("extra") #used for adding an ectra element to the user
    # #request for example "hello" will show up in the extracted element
    # if extra:
    #     user_data["extra"] = extra #for implementing the extra element in the output
 # return#200 is the default status for passing the json file
#"get-user/123?extra=hello world"
# print("yuegfuigeiufgeufh")
#@app.route("/create-user", methods =["POST"]) #another app route for the post method
# this is  a mtehod the user uses to add data to the db or create a resource we can run get and post in this path
#def create_user(): #us used another function create_user for the post method
    #can use if statement if there afre multiple (post) methods
    #data = request.get_json() #gives the body of the json file that was requested by the user(user data or input)
   # return jsonify(data), 201 #returns the result in jsonfied format
# print("yuegfuigeiufgeufh")

#if __name__ == "__main__":
  #  app.run(debug=True)
