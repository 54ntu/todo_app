import React from 'react'
import { Toolbar,AppBar,styled, Box } from '@mui/material';
import TaskForm from './components/taskForm';

function App() {
  const StyledToolbar =styled(Toolbar)({
    display:'flex',
    justifyContent:'space-between',

  });
  return (
    <div className="App">
      <AppBar position="static">
        <StyledToolbar>
          <Box>TODO</Box>
        </StyledToolbar>
      </AppBar>
      <TaskForm/>
    </div>
  );
}

export default App;
