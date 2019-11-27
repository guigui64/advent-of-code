import {withRouter} from 'next/router';
import Link from 'next/link';

let days = [];
for (let day=1; day<=25; day++) {
  days.push(day);
}

const Page = withRouter((props) => (
  <div>
    <h1>Solutions for year {props.router.query.year}</h1>
    <ul>
      {
        days.map((day) =>
          (
            <li>
              <Link href={`/${props.router.query.year}-${day}`}><a>{day}</a></Link>
            </li>
          ))
      }
    </ul>
  </div>
));

export default Page;
