import { useEffect } from 'react';

import MainLayout from './MainLayout';
import Pagination from './Pagination';

/*
 * Props are :
 *  years : array of years
 *  year : the year of the page
 *  day : the day of the page
 *  title : the title of the page
 *  input : the default input
 *  handleInputChange : fct
 *  solveAll : fct
 *  solutionPartX : solution of part X as text
 */
const DayLayout = (props) => {

  useEffect(() => document.title = 'AoC ' + props.year + '/' + props.day,[]);

  const copyTextToClipboard = (text) => {
    // Create new element
    var el = document.createElement('textarea');
    // Set value (string to be copied)
    el.value = text;
    // Set non-editable to avoid focus and move outside of view
    el.setAttribute('readonly', '');
    el.style = {position: 'absolute', left: '-9999px'};
    document.body.appendChild(el);
    // Select text inside element
    el.select();
    // Copy text to clipboard
    document.execCommand('copy');
    // Remove temporary element
    document.body.removeChild(el);
  };

  const copySolToClipboard = (event, output) => {
    copyTextToClipboard(output.value);
    event.target.focus();
  }

  let refOutput1, refOutput2;

  return (
    <MainLayout years={props.years} activeYear={props.year}>
      <Pagination year={props.year} currentDay={props.day} />
      <hr />
      <h4 class="text-center">Advent of Code {props.year} - Day {props.day} : {props.title}</h4>
      <div class="form-group">
        <label for="inputTextarea">Puzzle input</label>
        <textarea class="form-control" id="inputTextarea" rows="8"
          style={{fontFamily: 'monospace'}}
          placeholder="Copy input here."
          value={props.input}
          onChange={props.handleInputChange} />
      </div>
      <div class="form-group">
        <button class="btn btn-primary" onClick={props.solveAll}>Solve day</button>
      </div>
      <div class="form-group">
        { props.solutionPart1 !== '' && 'Part 1' }
        <output style={{fontFamily: 'monospace', paddingLeft: 16, paddingRight: 16}}
          ref={(output1) => refOutput1 = output1}>{props.solutionPart1}</output>
        {
          (typeof props.solutionPart1 !== 'undefined') && props.solutionPart1 != '' && document.queryCommandSupported('copy') &&
            <button class="btn btn-outline-primary btn-sm" onClick={(e) => copySolToClipboard(e, refOutput1)}>Copy</button>
        }
      </div>
      <div class="form-group">
        { props.solutionPart1 !== '' && 'Part 2' }
        <output style={{fontFamily: 'monospace', paddingLeft: 16, paddingRight: 16}}
          ref={(output2) => refOutput2 = output2}>{props.solutionPart2}</output>
        {
          (typeof props.solutionPart2 !== 'undefined') && props.solutionPart2 != '' && document.queryCommandSupported('copy') &&
            <button class="btn btn-outline-primary btn-sm" onClick={(e) => copySolToClipboard(e, refOutput2)}>Copy</button>
        }
      </div>
    </MainLayout>
  );
};

export default DayLayout;
