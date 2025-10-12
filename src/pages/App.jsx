import React from 'react';
import { Routes, Route } from "react-router-dom";
import NotFound from "./NotFound";
import GreetingClock from '../components/GreetingClock';

export default function App(){
  return (
    <div style={{padding:20}}>
      <header style={{display:'flex', justifyContent:'space-between', alignItems:'center', gap:12}}>
        <h1 style={{margin:0,fontSize:18}}>My App</h1>
        <GreetingClock />
      </header>

      <main style={{marginTop:20}}>
        <Routes>
          {/* your other routes here */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
    </div>
  );
}
