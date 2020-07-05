import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component{
    sendMessage(text){
        let textEntry = document.getElementById("entry_submission").value;
        let tableEntry = document.getElementById("convo_history");
        let firstRow = tableEntry.insertRow();
        let firstCell = firstRow.insertCell(0);
        firstCell.innerHTML = textEntry;
        let xhr = new XMLHttpRequest();
        let params = {
            "text": textEntry
        };
        let readyStateChanged = false;
        xhr.onreadystatechange = function(){
            console.log("Status: ", xhr.status);
            console.log("Response: ", xhr.responseText);
            console.log("Message Sent");

            if (xhr.status === 200 && !readyStateChanged) {
                let responseRow = tableEntry.insertRow();
                let responseCell = responseRow.insertCell();
                responseCell.innerHTML = "Response";
                readyStateChanged = true;
            }

        };

        xhr.open(
            "POST",
            'http://localhost:8082/message');
        xhr.setRequestHeader("content-type", "application/json");
        xhr.send(params);
    }

  render(){
    return (
      <div
          className="App">
        <header className="App-header">
          <p>
            Conversational AI
          </p>
        </header>
        <div className="row">
            <div
                className="column"
                style={{backgroundColor: "#abb"}}>
                <h2>Text Series</h2>
                <textarea
                    defaultValue="Enter Text Here"
                    id="entry_submission"/>
                <button
                    onClick={this.sendMessage}>Send to Server</button>
                <hr></hr>
                <table id="convo_history">
                </table>
            </div>
            <div
                className="column"
                style={{backgroundColor: "#bbb"}}>
                <h2>Meta-Data Responses</h2>
            </div>
        </div>
      </div>

    );
  }
}


export default App;
