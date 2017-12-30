import React, { Component } from 'react';
import SimpleAppBar from './containers/appBar';
import Main from './containers/main';
import Intro from './containers/intro';
import BottomNavigation, { BottomNavigationButton } from 'material-ui/BottomNavigation';
import WebIcon from 'material-ui-icons/Web';
import GroupIcon from 'material-ui-icons/Group';



import './App.css';


class App extends Component {
  state = {
    value: 0,
  };

  handleChange = (event, value) => {
    this.setState({ value });
  };

  render() {
    const { value } = this.state;
    return (
      <div className="App">
        <SimpleAppBar />
        {this.state.value === 0 
            ? <Main />
            : <Intro />
        }
        <BottomNavigation
            value={value}
            onChange={this.handleChange}
            showLabels
            id ="footer"
        >
            <BottomNavigationButton label="系统演示" icon={<WebIcon />} />
        <BottomNavigationButton label="项目说明" icon={<GroupIcon />} />
        </BottomNavigation>

      </div>
    );
  }
}

export default App;
