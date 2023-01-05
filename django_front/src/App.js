import React from "react";
import styled from "styled-components";

const StyledHello = styled.h1`
  color: red;
`;

const App = () => {
  return (
    <div>
      <StyledHello>Hello, world!</StyledHello>
    </div>
  );
};

export default App;
