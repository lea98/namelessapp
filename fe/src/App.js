import React from 'react';
import './App.css';
import {PostsComponent} from './posts'



function App() {



  return (    
    <div className="bg-light">
        <PostsComponent  className='border border-secondary col-3 py-2 my-4 mx-auto'/>
    </div>
  );
}

export default App;
