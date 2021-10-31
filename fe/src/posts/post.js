import React, {useState} from 'react'
import {ActionButton} from './buttons'

function getLastNumber(url) {
  var matches = url.match(/\d+/g);
  return matches[matches.length - 1];
}


 function UserImage(props){
  
  const handleImageClick=(event)=>{
    event.preventDefault() //call endpoint http://127.0.0.1:8000/profile/api/lea
    window.location.href=`/profile/${props.post.creator.username}`
   //console.log(props.post.creator.profile_image)
  }

   return <div>
     {props.post.creator.profile_image?<img alt='' onClick={handleImageClick}  className='rounded-circle' style={{cursor: 'pointer',height:'55px',width:'55px'}} src={`http://localhost:8000${props.post.creator.profile_image}`}></img>:
     <span style={{cursor: 'pointer'}} onClick={handleImageClick} className='py-3 px-3  rounded-circle bg-info'>{props.post.creator.username}
    </span> }
    </div>
 }


function convertTimestamp(timestmp){
  let dateAndTime=timestmp.split('T')
  let date=dateAndTime[0]
  
  let time=dateAndTime[1].split('.')
  return [date,time[0]]
  }

export function Post(props){
  const {post, className}=props
  const [actionPost, setActionPost]=useState(props.post ? props.post :null)

  const url=window.location.href
  const idFromUrl=getLastNumber(url)
  const alreadyInDetail= post.id === parseInt(idFromUrl)

  

  const handlePerformAction=(newActionPost,status)=>{
    if(status===200){
      //console.log(post.creator)
    setActionPost(newActionPost)
    }
    console.log(post.creator)
  }

  const handlePostDetailClick=(event)=>{

    event.preventDefault()
    window.location.href=`/${post.id}`
  }

//   const handleDeleteClick = (e)=>{
//     e.preventDefault()
//     deletePost(post.id, (response,status)=>{ 
//       if (status===200){
//       alert('Post deleted')
//     }
//     else{
//       alert('Error')
//   }
//     })

// }

  let convertedTime=convertTimestamp(post.timestamp)

    return <div className={className}>
  <UserImage post={post} ></UserImage>
  <p className='mt-3'>{post.creator.username}</p>
  <p className='mt-3'>#{post.id}</p>
  <p className='mt-3'>{post.content}</p>

  {alreadyInDetail===false?null: <div>
<div>{post.creator.first_name}{' '}{post.creator.last_name}</div>
<div>{post.creator.email}</div>

  <div style={{marginBottom:'0.5em'}}>{convertedTime[0]}{', '}{convertedTime[1]}</div>
</div>}
       
      <ActionButton style={{margin:'0.2em'}} post={actionPost} didPerformAction={handlePerformAction} action={{type: "like"}}></ActionButton>
      <ActionButton style={{margin:'0.2em'}} post={actionPost} didPerformAction={handlePerformAction}  action={{type: "dislike"}}></ActionButton>

      {alreadyInDetail===true?null: <button style={{float:'left',marginRight:'0.2em',backgroundColor:'Indigo'}} className='btn btn-secondary' onClick={handlePostDetailClick}>See more</button>}
       
     {props.loggedUser===post.creator.username?<span className='float-right' style={{cursor: 'pointer',color:'Indigo'}}  onClick={() => props.handleDeletePost(post.id)} ><svg width="2em" height="2em" viewBox="0 0 16 16" className="bi bi-trash" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
  <path fillRule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4L4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
</svg></span>:null
}
</div>
  }
  



  