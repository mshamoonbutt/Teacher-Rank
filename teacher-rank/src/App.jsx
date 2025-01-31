import Header from "./Header.jsx"
import Body from "./Body.jsx"
import Option from "./Siginup-option.jsx"
import Siginup from "./siginup.jsx"
import Login from "./login.jsx"
import Home from "./Home.jsx"
import Course from "./courses.jsx"
import Teacher from "./Teacher.jsx"
import Rating from "./Viewrating.jsx"
function App() {
  const styles = {
    backgroundColor : "purple",
    minHeight: "100vh",
    margin : "0%"
  }
  return (
    <body style={styles}>
        <Header/>
        <Body/>
    </body>
  )
};
export default App
