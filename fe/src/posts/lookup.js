import {lookup} from '../lookup'

export function loadingPosts(username,callback){ //postslist
  let endpoint =  "/api/posts/" //leave like this, not if else
  if (username){
      endpoint =  `/api/posts/?username=${username}`
  }
  lookup("GET", endpoint, callback)
   }
 
export function detailView(id,callback){ //postslist

    lookup('GET',`/api/posts/${id}/`,callback)
  
     }

 export function createPost(newPost,callback){
   lookup('POST', '/api/posts/create', callback, {content:newPost})
 }
 
 export function likePost(id, action, callback){
   lookup('POST', '/api/posts/action', callback,{id:id, action:action})
 }


 export function deletePost(id, callback){
  lookup('DELETE', `/api/posts/${id}/delete`, callback,{id:id})
}


