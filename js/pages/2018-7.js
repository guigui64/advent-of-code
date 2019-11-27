import { useState } from 'react';

import DayLayout from '../components/DayLayout';
import * as aoc from '../aoc/2018-7';

const Page = (props) => {
  const [input, setInput] = useState(`Step P must be finished before step O can begin.
Step H must be finished before step X can begin.
Step M must be finished before step Q can begin.
Step E must be finished before step U can begin.
Step G must be finished before step O can begin.
Step W must be finished before step F can begin.
Step O must be finished before step F can begin.
Step B must be finished before step X can begin.
Step F must be finished before step C can begin.
Step A must be finished before step L can begin.
Step C must be finished before step D can begin.
Step D must be finished before step Y can begin.
Step V must be finished before step R can begin.
Step I must be finished before step Y can begin.
Step X must be finished before step K can begin.
Step T must be finished before step S can begin.
Step Y must be finished before step J can begin.
Step Z must be finished before step R can begin.
Step R must be finished before step K can begin.
Step K must be finished before step N can begin.
Step U must be finished before step N can begin.
Step Q must be finished before step N can begin.
Step N must be finished before step J can begin.
Step S must be finished before step J can begin.
Step L must be finished before step J can begin.
Step A must be finished before step C can begin.
Step S must be finished before step L can begin.
Step X must be finished before step S can begin.
Step T must be finished before step J can begin.
Step B must be finished before step C can begin.
Step G must be finished before step N can begin.
Step M must be finished before step O can begin.
Step Y must be finished before step K can begin.
Step B must be finished before step Y can begin.
Step Y must be finished before step U can begin.
Step F must be finished before step J can begin.
Step A must be finished before step N can begin.
Step W must be finished before step Y can begin.
Step C must be finished before step R can begin.
Step Q must be finished before step J can begin.
Step O must be finished before step L can begin.
Step Q must be finished before step S can begin.
Step H must be finished before step E can begin.
Step N must be finished before step S can begin.
Step A must be finished before step T can begin.
Step C must be finished before step K can begin.
Step Z must be finished before step J can begin.
Step U must be finished before step Q can begin.
Step B must be finished before step F can begin.
Step W must be finished before step X can begin.
Step H must be finished before step Q can begin.
Step B must be finished before step V can begin.
Step Z must be finished before step U can begin.
Step O must be finished before step A can begin.
Step C must be finished before step I can begin.
Step I must be finished before step T can begin.
Step E must be finished before step D can begin.
Step V must be finished before step S can begin.
Step F must be finished before step V can begin.
Step C must be finished before step S can begin.
Step I must be finished before step U can begin.
Step F must be finished before step Z can begin.
Step A must be finished before step X can begin.
Step C must be finished before step N can begin.
Step G must be finished before step F can begin.
Step O must be finished before step R can begin.
Step V must be finished before step X can begin.
Step E must be finished before step A can begin.
Step K must be finished before step Q can begin.
Step Z must be finished before step K can begin.
Step T must be finished before step K can begin.
Step Y must be finished before step Z can begin.
Step W must be finished before step B can begin.
Step E must be finished before step V can begin.
Step W must be finished before step J can begin.
Step I must be finished before step S can begin.
Step H must be finished before step L can begin.
Step G must be finished before step I can begin.
Step X must be finished before step L can begin.
Step H must be finished before step G can begin.
Step H must be finished before step Z can begin.
Step H must be finished before step N can begin.
Step D must be finished before step I can begin.
Step E must be finished before step J can begin.
Step X must be finished before step R can begin.
Step O must be finished before step J can begin.
Step N must be finished before step L can begin.
Step X must be finished before step N can begin.
Step V must be finished before step Q can begin.
Step P must be finished before step Y can begin.
Step H must be finished before step U can begin.
Step X must be finished before step Z can begin.
Step G must be finished before step Q can begin.
Step B must be finished before step Q can begin.
Step Y must be finished before step L can begin.
Step U must be finished before step J can begin.
Step W must be finished before step V can begin.
Step G must be finished before step C can begin.
Step G must be finished before step B can begin.
Step O must be finished before step B can begin.
Step R must be finished before step N can begin.`);
  const [solutionPart1, setSolutionPart1] = useState('');
  const [solutionPart2, setSolutionPart2] = useState('');

  return (
    <DayLayout
      years={[2018, 2017, 2016, 2015]}
      year={2018}
      day={7}
      title="The Sum of Its Parts"
      input={input}
      handleInputChange={e => {
        setInput(e.target.value);
        setSolutionPart1('');
        setSolutionPart2('');
      }}
      solveAll={() => {
        const [part1, part2] = aoc.all(input);
        setSolutionPart1(part1);
        setSolutionPart2(part2);
      }}
      solutionPart1={solutionPart1}
      solutionPart2={solutionPart2}
    />
  );
}

export default Page;
