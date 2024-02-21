class MRole:  
        id:any
        name:any;

class MMenu:  
        id:any
        name:any;

class MCategory:  
        id:any
        name:any;

class MGenre:  
        id:any
        name:any;

class RRoleMenu:  
        id:any
        id_role:any
        id_menu:any; 

class MUser:  
        id:any
        id_role: any
        username:any     
        password:any
        ktp:any;

class MCatalogue:  
        id:any
        id_category: any
        title:any
        published_date:any
        writer:any
        capacity:any
        max_day_loans:int

class TTransaction:  
        id:any
        id_user:any
        id_catalogue:any
        start_loans_date:any
        end_loans_date:any
        loans_day:any;
        is_returned:any

class CatalogueDetail:  
        no:any
        judul: any
        genre:any
        penulis:any;
        tanggal_terbit:any
        unit:any
        maks_hari_peminjaman:any
        id:any