import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/Header';
import DashBoard from './todo/DashBoard';

// import { Provider } from 'react-redux';
// import store from '../store';

class App extends Component {
    render() {
        return (
            <Fragment>
                <Header/>
                <DashBoard/>
            </Fragment>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));