import React, { Component } from "react";
import ReactDOM from 'react-dom'
import { JournalEntry } from "./entry";

export default class JournalList extends Component {
    constructor(props) {
      super();
  
      this.state = {
        journalData: [],
        isOpen: true
      };
  
      this.clearEntries = this.clearEntries.bind(this)
      this.showAllEntries = this.showAllEntries.bind(this)
      this.toggleStatus = this.toggleStatus.bind(this)
    }
    
    componentDidMount() {
        fetch("http://127.0.0.1:5000/entries")
        .then(res => res.json())
        .then(
            (result) => {
                this.setState({
                    journalData: result.items
                });
            }
        )
    }


    clearEntries(){
      this.setState({ journalData: [], isOpen: false });
    };
  
    showAllEntries(){
      this.setState({ journalData: rawJournalData, isOpen: true });
    };
  
    toggleStatus(){       
      if (this.state.isOpen) {
        this.setState({ journalData: [], isOpen: false });
      } else {
        this.setState({ journalData: rawJournalData, isOpen: true });
      }
    };
  
    render() {
      const journalEntries = this.state.journalData.map(journalEntry => {
        return (
          <div key={journalEntry.title}>
            <JournalEntry
              title={journalEntry.title}
              content={journalEntry.content}
            />
          </div>
        );
      });
  
      return (
        <div>
          <h1>{this.props.heading}</h1>
          {journalEntries}
          <button onClick={this.clearEntries}>Clear Journal Entries</button>
          <button onClick={this.showAllEntries}>Show All Journal Entries</button>
        </div>
      );
      
    }
  }