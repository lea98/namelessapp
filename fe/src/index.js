import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import {PostsComponent, PostDetail} from './posts'

if (document.getElementById('root')){
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);}

const postsComp = document.getElementById('postsComp')
const e=React.createElement
if(postsComp){ //i want to show this on django runpage
  //console.log(document.getElementById('postsComp').dataset) //built in property that alllows us to see everything hats added to element e.g. data-username
  
  //pass in arguments you want to add as props, e.g. dict postsComp.dataset
  ReactDOM.render(e(PostsComponent,postsComp.dataset),postsComp);}


  const postsDetail = document.querySelectorAll('.post-detail')
  postsDetail.forEach(container=>{
    ReactDOM.render(e(PostDetail,container.dataset),container);} //insert into individaul container it is looping through

  )


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
