import Header from "./components/Header";
import App_Router from "./router/App_Router";

const App = () => {
  return (
    <div className="App container">
      <Header />
      <App_Router />
    </div>
  );
};

export default App;
