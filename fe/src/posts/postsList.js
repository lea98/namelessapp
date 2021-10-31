import React, {useEffect, useState} from 'react'
import {loadingPosts} from './lookup'
import {Post} from './post'
import {deletePost} from './lookup'

  export function PostsList(props){
    const [postsInit, setPostsInit]=useState([])
    const [posts, setPosts]=useState([])
    //loadindPosts ce trigerat GET stalno cause i dont have condition. add:
    const [postsDidSet,setPostsDidSet]=useState(false)


    //console.log(props.newPost)
   // setPostsInit([...props.newPost].concat(postsInit)) //concatenate with initial posts. gives infinite loop without useEfect and other list(2.line)
    useEffect(()=>{
      const final=[...props.newPosts].concat(postsInit)
      if (final.length!==posts.length){
        setPosts(final)
      }
    },[props.newPosts,posts,postsInit])


    useEffect(()=>{
      if(postsDidSet===false){
      const handleloadingPosts=(response,status)=>{
        if(status===200){
        setPostsInit(response)
        setPostsDidSet(true)
        }else{
          alert('error')
        }
      }
      loadingPosts(props.username,handleloadingPosts) //null for username as default
    }
    },[postsInit,postsDidSet,setPostsDidSet,props.username]) //also pass props.username as dependency
  


    const handleDeletePost = (id) => {
      setPostsInit(posts.filter((post) => post.id !== id))
      deletePost(id,handleLookup)
       console.log(id)
    }
    const handleLookup=(response,status)=>{
      if (status===200){
        alert('Post Deleted')
        console.log(response,status)
      }
      else{
        alert('Post not found')
      }
    }
  

    return posts.map((item)=>{
      return <Post 
      className='border border-primary col-xs-12 col-md-8 col-lg-5 py-5 my-5 mx-auto' post={item} key={item.id}  
      handleDeletePost={handleDeletePost} loggedUser={props.loggedUser}></Post> //{item.id}?
    })
  }