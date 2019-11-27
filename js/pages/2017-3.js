import DayLayout from '../components/DayLayout';
import * as aoc from '../aoc/2017-3';

class Page extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: `265149`,
      solutionPart1: '',
      solutionPart2: '',
    };

    this.handleInputChange = this.handleInputChange.bind(this);
    this.solveAll = this.solveAll.bind(this);
  }

  handleInputChange(event) {
    this.setState({
      input: event.target.value,
      solutionPart1: '',
      solutionPart2: '',
    });
  }

  solveAll() {
    const [part1, part2] = aoc.all(this.state.input);
    this.setState({solutionPart1: part1, solutionPart2: part2});
  }

  render() {
    return (
      <DayLayout
        years={[2018, 2017, 2016, 2015]}
        year={2017}
        day={3}
        title="Spiral Memory"
        input={this.state.input}
        handleInputChange={this.handleInputChange}
        solveAll={this.solveAll}
        solutionPart1={this.state.solutionPart1}
        solutionPart2={this.state.solutionPart2}
      />
    );
  }
}

export default Page;

