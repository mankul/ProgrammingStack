
template<class Container, class T>
auto addOperation(Container && C, T & t) -> decltype(std::forward<Container> (C)[t]){
    return std::forward<Container> (C)[t];
}