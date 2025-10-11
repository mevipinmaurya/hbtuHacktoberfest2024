import React, { useState } from 'react';
import '../styles/Modal.css';

const Modal = ({content}) => {
    [open,setOpen]=useState(false);

    function close(){
        setOpen(false);
    }

  return (
    <div className={open?'content-wrapper':'closed'}>
      {content}
      <button onClick={close} ></button>
    </div>
    
  );
};

export default Modal;
