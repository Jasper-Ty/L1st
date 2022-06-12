package L1st;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.ListIterator;

/**
 * ArrayList wrapper that begins indexing at 1
 */
public class ArrayL1st<E> extends ArrayList<E> {

    public ArrayL1st(int initialCapacity) {
        super(initialCapacity);
    }

    public ArrayL1st() {
        super();
    }

    public ArrayL1st(Collection<? extends E> c) {
        super(c);
    }

    @Override
    public E get(int index) {
        return super.get(index - 1);
    }

    @Override
    public E set (int index, E element) {
        return super.set(index - 1, element);
    }

    @Override
    public void add(int index, E element) {
        super.add(index - 1, element);
    }

    @Override
    public E remove(int index) {
        return super.remove(index - 1);
    }

    @Override
    public boolean addAll(int index, Collection<? extends E> c){
        return super.addAll(index - 1, c);
    }

    @Override
    protected void removeRange(int fromIndex, int toIndex) {
        super.removeRange(fromIndex - 1, toIndex - 1);
    }

    @Override
    public ListIterator<E> listIterator(int index) {
        return super.listIterator(index-1);
    }

    @Override
    public List<E> subList(int fromIndex, int toIndex) {
        return super.subList(fromIndex - 1, toIndex - 1);
    }
    
    @Override
    public int indexOf(Object o) {
        int idxOf = super.indexOf(o);
        return idxOf >= 0 ? idxOf : -1;
    }

    @Override
    public int lastIndexOf(Object o) {
        int lastIdxOf = super.indexOf(o);
        return lastIdxOf >= 0 ? lastIdxOf : -1;
    }

}

