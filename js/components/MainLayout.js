import 'bootstrap/dist/css/bootstrap.min.css';
import Link from 'next/link';

/*
 * Props are :
 *  years : array of years
 *  activeYear
 */
const MainLayout = (props) => (
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <Link href="/index"><a class="navbar-brand" href="#">Advent of code solutions</a></Link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          {props.years.map((year) => (

            <li class={'nav-item' + (year == props.activeYear ? ' active' : '')} key={year}>
              <Link href={`/${year}-1`}><a class="nav-link" href="#">
                  {year}
                  {year == props.activeYear &&
                      <span class="sr-only">(current)</span>
                  }
              </a></Link>
            </li>
          ))}
        </ul>
      </div>
    </nav>
    <div class="container" style={{padding: 16}}>
      {props.children}
    </div>
  </div>
);

export default MainLayout;
