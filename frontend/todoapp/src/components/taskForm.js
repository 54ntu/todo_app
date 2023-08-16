import { Box, styled } from '@mui/material';
import { red } from '@mui/material/colors';
import React from 'react'

const TaskForm = () => {
    const StyedBox = styled(Box)({
        height:300,
        width:400,
        backgroundColor:red,


    });
  return (<StyedBox>this is form</StyedBox>);
}

export default TaskForm;