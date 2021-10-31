import React from 'react'
import {likePost} from './lookup'

export function ActionButton(props){
    const {post, className, action, didPerformAction}=props
    const likes=post.likes ? post.likes : 0
   // const [userLike, updateUserLike] = useState(post.userLike === true ? true : false)

    //callback

    const handleLikePostCallback=(response,status)=>{
      if((status===200||status===201)&&didPerformAction){
        //updateLikes(response.likes)
        didPerformAction(response,status)
        //updateUserLike(true)
      }
    //   if(action.type==='like'){
    //     if (userLike === true) {
    //         // perhaps i Unlike it?
    //         updateLikes(likes - 1)
    //         updateUserLike(false)
    //       } else {
    //         updateLikes(likes + 1)
    //         updateUserLike(true)
    //       }
    // }
    }

    const handleLikeClick=(e)=>{
        e.preventDefault()
        likePost(post.id,action.type,handleLikePostCallback)

    }
   const display = action.type === 'like' ? `${likes}` : ''
   const upDown = action.type === 'like' ? "fa fa-thumbs-up":"fa fa-thumbs-down"

      return  <span style={{margin:'0.2em'}}>
      <button style={{color:'Indigo'}} className={className} onClick={handleLikeClick} > {display} <i className={upDown} style={{fontSize:'30px'}} ></i> </button> 
      </span>
   }
  