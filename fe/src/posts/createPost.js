import React from 'react'
import {createPost} from './lookup'


  export function CreatePost(props){

    const textareaReference = React.createRef()
    const { didPost}=props
   // const {username}=props insted passing username={username} delete this and ass ...props
    //console.log(props) valid and username
    const handleSubmit = (e)=>{
        e.preventDefault()
        const newPostValue=textareaReference.current.value //text from textearea
       // let tempNewPost = [...newPost] //copy posts list? temporary list so i can set new list based on new state?? (list or array)
        createPost(newPostValue, (response,status)=>{ //response,status as callback
          if (status===201){
          didPost(response)

        }
        else{
          alert('error')
          console.log(response)
      }
        })
    
        textareaReference.current.value=''

    }
//if has permission allow div to be rendered
    return <div className='col-12 mb-4'>
    <form className='' onSubmit={handleSubmit}>
      <div className='d-flex justify-content-center'>
    <textarea required={true} ref={textareaReference}>
    </textarea>
    <button type='submit' className='btn btn-secondary' style={{marginLeft:'0.3em',backgroundColor:'Indigo'}}>POST</button>
    </div>
</form>
</div>
}