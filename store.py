class Post:
    
    def __init__(self,id,name,photo_url,body):
        self.id=id
        self.name=name
        self.photo_url=photo_url
        self.body=body

posts=[]
class PostStore:
        
    def get_all(self):
        return posts

    def add(self,post):
        posts.append(post) 
        return posts

    def get_by_id(self,id):

        result=None

        for post in posts:
            if post.id==id:
               result=post
               break
        return result     
 
    def update(self,id,fields):
        post=self.get_by_id(id)
        post.name=fields["name"]
        post.photo_url=fields["photo_url"]
        post.body=fields["body"]
        return post    


    def delete(self,id):
        post=self.get_by_id(id)   
        posts.remove(post)
        return posts