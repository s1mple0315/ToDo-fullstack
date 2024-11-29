import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Register_page from "../pages/Register_page";
import Main_page from "../pages/Main_page";
import Login_page from "../pages/Login_page";

const App_Router = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Main_page />} />
        <Route path="/register" element={<Register_page />} />
        <Route path="/login" element={<Login_page />} />
      </Routes>
    </Router>
  );
};

export default App_Router;
