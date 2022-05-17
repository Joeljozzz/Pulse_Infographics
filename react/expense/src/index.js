import React from 'react';
import ReactDom from 'react-dom';
import App from './App';
import { Provider } from './context/context';
import { SpeechProvider } from '@speechly/react-client';
import './index.css'

ReactDom.render(<SpeechProvider appId="f533a0d0-53de-40be-8dd5-cb583174d75c" language="en-US"> <Provider><App /> </Provider> </SpeechProvider>, document.getElementById('root'));