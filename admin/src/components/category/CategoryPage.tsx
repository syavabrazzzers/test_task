import React, {useEffect, useState} from 'react';
import axios from "axios";
import {Pagination} from "@mui/material";
import Category from "./Category";
import {ICategory, NewCategory} from "./interfaces";



const CategoryPage = () => {

  const [parents, setParents] = useState<Array<ICategory>>([])
  const [page, setPage] = useState(1)
  const [reload, setReload] = useState(false)
  const [addCategory, setAddCategory] = useState(false)


  let new_category: NewCategory = {
    name: '',
    parent: 0,
    file: null
  };


  useEffect(() => {
    axios.get(`http://localhost:8000/category/tree/${page}`).then((response) => {
      console.log(response.data)
      setParents(response.data)
    })
      .catch((response) => {
        if (response.status === 404) {
          setParents([])
        }
      })
  }, [page, reload])

  const createCategory = () => {
    if (new_category.name && new_category.parent && new_category.file){
      let formData = new FormData()
      formData.append('file', new_category.file, new_category.file.filename)
      formData.append('category', JSON.stringify({name: new_category.name, parent: new_category.parent}))

      axios.put('http://localhost:8000/category/create', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'accept': 'application/json'
        }
      })
        .then((response) => {
          alert('Добавлено')
          setAddCategory(false)
          setReload(prev => !prev)
        })
        .catch((response) => {
          alert(response.status)
        })
    }
    console.log(new_category)
  }

  return (
    <div className={`w-full h-full border flex flex-col justify-center items-center p-3`}>
      <Pagination count={10} onChange={(event, value) => setPage(value)}/>
      <table className={`w-full`}>
        <thead className={`w-full`}>
          <tr>
            <th><div>id</div></th>
            <th><div>name</div></th>
            <th><div>slug</div></th>
            <th><div>parent</div></th>
            <th><div>parent_category</div></th>
            <th><div>image</div></th>
            <th></th>
          </tr>
        </thead>
        <tbody className={`w-full`}>
        {parents.length > 0 ? parents.map((value, key) => {
          return <Category value={value} key={key} setReload={setReload}/>
        }) : <tr>Not found</tr>}
        {addCategory && <tr>
            <td className={`text-center`}></td>
            <td className={`text-center`}>
                <input className={`border`} type="text" placeholder={`Name`} onChange={(event) => {
                  new_category.name = event.target.value
                }}/>
            </td>
            <td className={`text-center`}></td>
            <td className={`text-center`}>
                <input className={`border`} type="number" placeholder={`Parent`} onChange={(event) => {
                  new_category.parent = parseInt(event.target.value)
                }}/>
            </td>
            <td className={`text-center`}></td>
            <td className={`text-center`}>
                <input className={`border`} type="file" onChange={(event) => {
                  if (event.target.files) {
                    new_category.file = event.target.files[0]
                  }
                }}/>
            </td>
            <td className={`border text-center`} onClick={createCategory}>+</td>
        </tr>}
        </tbody>
      </table>
      <div className={`mt-3 p-2 rounded border`} onClick={() => setAddCategory(prev => !prev)}>+</div>
    </div>
  );
};

export default CategoryPage;