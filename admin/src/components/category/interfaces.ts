import {Dispatch, SetStateAction} from "react";

export interface ICategory {
  id: number,
  name: string,
  slug: string,
  parent: string,
  parent_category: string,
  image: string
}

export interface NewCategory {
  name: string,
  parent: number,
  file: any
}

export interface EditCategory {
  name: string,
  slug: string,
  parent: number,
  file: any
}

export interface ICategoryProps {
  value: ICategory,
  key: number,
  setReload: Dispatch<SetStateAction<boolean>>
}