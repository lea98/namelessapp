import React, {useState, useEffect} from 'react'
import {PostsList} from './postsList'
import {CreatePost} from './createPost'
import {detailView} from './lookup'
import {Post} from './post'

export function PostDetail(props){
  const {id}=props
  const [didLookup, setDidLookup]=useState(false)
  const [post,setPost]=useState(null)
  //callback handler:
  const handleLookup=(response,status)=>{
    if (status===200){
      setPost(response)
    }
    else{
      alert('Post not found')
    }
  }

  useEffect(()=>{
    if (!didLookup){
      detailView(id,handleLookup)

      setDidLookup(true)
    }
  },[id, didLookup, setDidLookup] )

  return post===null?null : <Post post={post}/>
}


  export function PostsComponent(props){
    //const {hasPermission} = props //from index.html data-has-permission (not built in)
    const hasPermission=props.hasPermission==='false' ? false:true //cause its a string there
    const loggedUser=props.loggedUser//cause its a string there

    const [newPosts, setNewPosts] = useState([]) //create a state comp inside parent component(Posts)
   // const {username}=props insted passing username={username} delete this and ass ...props
    //console.log(props) valid and username
    const handleSubmit = (newPost)=>{
        let tempNewPosts = [...newPosts] //copy posts list? temporary list so i can set new list based on new state?? (list or array)
          tempNewPosts.unshift(newPost) //unshift ka push al na pcoetak?
          setNewPosts(tempNewPosts)        
    }


//if has permission allow div to be rendered
    return <div className={props.className}>
        {hasPermission===true&& <CreatePost didPost={handleSubmit} className='col-12 mb-3'/>}
    <PostsList newPosts={newPosts} {...props} loggedUser={loggedUser}/>
    </div>
  }


 