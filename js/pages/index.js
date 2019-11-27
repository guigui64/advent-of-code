import { useEffect } from 'react';
import MainLayout from '../components/MainLayout';

const Index = () => {
  useEffect(() => document.title = 'AoC solutions', []);
  return (
    <MainLayout years={[2018, 2017, 2016, 2015]}>
      <p>Choose a year in the navigation bar.</p>
    </MainLayout>
  );
};

export default Index;
