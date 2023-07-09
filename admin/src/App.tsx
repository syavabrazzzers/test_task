import React, {useEffect, useState} from 'react';
import Header from "./components/Header";
import CategoryPage from "./components/category/CategoryPage";

export enum Page {
  category,
  products
}

function App() {
  // const [page, setPage] = useState<Page>(Page.category)

  return (
    <div className="app">
      {/*<Header setPage={setPage}/>*/}
      <CategoryPage/>
      {/*{page === Page.category ? <CategoryPage/> : <ProductsPage/>}*/}
    </div>
  );
}

export default App;
